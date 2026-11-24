"""DialogFrame カセットの config ・素材 ・本文の参照が整合しているか検証します。

config は実行せず AST からリテラル値だけを読み込みます。
エラーにはファイル名 ・行番号 ・素材名だけを含め、本文の内容は含めません。
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any

REQUIRED_KEYS = (
    "cassette",
    "maintextName",
    "imageConf",
    "imageOpenName",
    "seConf",
    "soundTurnPage",
    "bgmConf",
    "dialogFont",
    "dialogIcon",
    "openingBackGroundImage",
    "openingBGM",
    "openingSound",
    "linkingList",
)
EVENT_PATTERN = re.compile(r"<event\s+([^>]*)>")
ATTRIBUTE_PATTERN = re.compile(r"""(\w+)(?:=("[^"]*"|'[^']*'|[^\s>]+))?""")
# event タグの属性と、その値を登録しておく config の項目の対応です。
EVENT_REFERENCES = {
    "image": (("file", "changefrom", "changeto"), "imageConf"),
    "sound": (("file",), "seConf"),
    "bgm": (("file",), "bgmConf"),
}


def file_exists(directory: Path, name: str) -> bool:
    """大文字小文字まで一致するファイルがあるか判定します。"""
    return directory.is_dir() and any(
        child.name == name and child.is_file() for child in directory.iterdir()
    )


def load_conf(config_path: Path) -> tuple[dict[str, Any], list[str]]:
    """config の class Conf にある代入をリテラルとして読み込みます。"""
    try:
        tree = ast.parse(config_path.read_text(encoding="utf-8"), filename=str(config_path))
    except (SyntaxError, UnicodeDecodeError) as error:
        return {}, [f"構文エラーです ({type(error).__name__})"]
    classes = [node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == "Conf"]
    if len(classes) != 1:
        return {}, ["class Conf がひとつではありません"]
    conf: dict[str, Any] = {}
    errors: list[str] = []
    for node in classes[0].body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if not isinstance(target, ast.Name):
                continue
            try:
                conf[target.id] = ast.literal_eval(node.value)
            except ValueError, TypeError, SyntaxError, RecursionError:
                errors.append(f"{target.id} がリテラルではありません")
    return conf, errors


def names_of(entries: Any) -> list[str]:
    return [entry["name"] for entry in entries]


def check_conf(cassette: Path, conf: dict[str, Any], add: Callable[[str], None]) -> None:
    if conf["cassette"] != cassette.name:
        add(f"config: cassette '{conf['cassette']}' がディレクトリ名と一致しません")

    images = names_of(conf["imageConf"])
    se = names_of(conf["seConf"])
    bgm = names_of(conf["bgmConf"])
    for entry in conf["imageConf"]:
        trans = entry["trans"]
        if trans is not False and not (
            isinstance(trans, tuple | list)
            and len(trans) == 2
            and all(type(value) is int for value in trans)
        ):
            add(f"config: imageConf '{entry['name']}' の trans は False か (x, y) にします")
    for directory, key, names in (
        ("image", "imageConf", images),
        ("sound", "seConf", se),
        ("sound", "bgmConf", bgm),
        ("other", "dialogFont", [conf["dialogFont"]]),
        ("other", "dialogIcon", [conf["dialogIcon"]]),
    ):
        for name in names:
            if not file_exists(cassette / directory, name):
                add(f"{directory}/{name}: {key} のファイルがありません")

    maintexts = conf["maintextName"]
    if isinstance(maintexts, list):
        buttons = conf.get("openingStartList", [])
        if len(buttons) != len(maintexts):
            add("config: openingStartList の数が maintextName の数と一致しません")
        button_refs = [("openingStartList", button) for button in buttons]
    else:
        maintexts = [maintexts]
        button_refs = [(key, conf.get(key, {})) for key in ("openingStart", "openingContinue")]
    for name in maintexts:
        if not file_exists(cassette / "maintext", name):
            add(f"maintext/{name}: maintextName のファイルがありません")

    image_refs = [
        ("imageOpenName", conf["imageOpenName"]),
        ("openingBackGroundImage", conf["openingBackGroundImage"]),
    ]
    image_refs += [(key, button[n]) for key, button in button_refs for n in ("name1", "name2")]
    image_refs += [
        ("linkingList", link[part])
        for links in conf["linkingList"]
        for link in links.values()
        for part in ("main", "back")
    ]
    refs = [(key, name, "imageConf", images) for key, name in image_refs]
    refs += [
        ("soundTurnPage", conf["soundTurnPage"], "seConf", se),
        ("openingSound", conf["openingSound"]["name"], "seConf", se),
        ("openingBGM", conf["openingBGM"]["name"], "bgmConf", bgm),
    ]
    for key, name, registry, registered in refs:
        if name not in registered:
            add(f"config: {key} の '{name}' が {registry} に登録されていません")

    registries = {"imageConf": images, "seConf": se, "bgmConf": bgm}
    for name in maintexts:
        check_maintext(cassette / "maintext" / name, registries, add)


def check_maintext(
    path: Path, registries: dict[str, list[str]], add: Callable[[str], None]
) -> None:
    if not path.is_file():
        return
    try:
        lines = path.read_bytes().decode("utf-8").splitlines()
    except UnicodeDecodeError:
        add(f"maintext/{path.name}: UTF-8 として読めません")
        return
    for number, line in enumerate(lines, start=1):
        for match in EVENT_PATTERN.finditer(line):
            attributes = {
                key: value.strip("\"'") for key, value in ATTRIBUTE_PATTERN.findall(match.group(1))
            }
            reference = EVENT_REFERENCES.get(attributes.get("name", ""))
            if reference is None:
                continue
            keys, registry = reference
            for key in keys:
                name = attributes.get(key)
                if name and name not in registries[registry]:
                    add(
                        f"maintext/{path.name}:{number}: {key} の '{name}' が "
                        f"{registry} に登録されていません"
                    )


def validate_cassette(cassette: Path) -> list[str]:
    """カセットを検証し、エラーメッセージの一覧を返します。"""
    errors: list[str] = []

    def add(message: str) -> None:
        errors.append(f"{cassette.name}: {message}")

    configs = sorted((cassette / "config").glob("*.py"))
    if len(configs) != 1:
        add(f"config: config/*.py がひとつではありません ({len(configs)} 件)")
        return errors
    conf, load_errors = load_conf(configs[0])
    for message in load_errors:
        add(f"config: {message}")
    if load_errors:
        return errors
    missing = [key for key in REQUIRED_KEYS if key not in conf]
    for key in missing:
        add(f"config: 必須項目 {key} がありません")
    if missing:
        return errors
    try:
        check_conf(cassette, conf, add)
    except (KeyError, TypeError, AttributeError) as error:
        add(f"config: 項目の形式が想定と異なります ({type(error).__name__}: {error})")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cassettes", nargs="*", help="検証するカセット名 (省略時は全カセット)")
    parser.add_argument(
        "--root", type=Path, default=Path.cwd(), help="カセットを置いたディレクトリ"
    )
    args = parser.parse_args(argv)
    root: Path = args.root

    if args.cassettes:
        targets = [root / name for name in args.cassettes]
    else:
        targets = sorted(path for path in root.glob("cassette-*") if path.is_dir())
    if not targets:
        print(f"{root}: カセットがありません")
        return 1

    failed = False
    for cassette in targets:
        if not cassette.is_dir():
            print(f"{cassette.name}: カセットがありません")
            failed = True
            continue
        errors = validate_cassette(cassette)
        print("\n".join(errors) if errors else f"{cassette.name}: OK")
        failed = failed or bool(errors)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
