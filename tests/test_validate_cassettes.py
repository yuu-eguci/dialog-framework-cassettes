"""tools/validate_cassettes.py のテストです。"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from tools.validate_cassettes import main, validate_cassette

REPO_ROOT = Path(__file__).resolve().parent.parent
NAME = "cassette-test"


def base_conf() -> dict[str, Any]:
    return {
        "cassette": NAME,
        "maintextName": "main.txt",
        "imageConf": [
            {"name": "bg.jpg", "trans": False},
            {"name": "chara.png", "trans": (0, 0)},
            {"name": "chara_back.png", "trans": False},
            {"name": "start1.png", "trans": False},
            {"name": "start2.png", "trans": False},
            {"name": "continue1.png", "trans": False},
            {"name": "continue2.png", "trans": False},
        ],
        "imageOpenName": "chara.png",
        "seConf": [{"name": "se.ogg"}],
        "soundTurnPage": "se.ogg",
        "bgmConf": [{"name": "bgm.mp3"}],
        "dialogFont": "font.ttf",
        "dialogIcon": "icon.png",
        "openingBackGroundImage": "bg.jpg",
        "openingBGM": {"name": "bgm.mp3", "volume": 0.5},
        "openingStart": {"name1": "start1.png", "name2": "start2.png"},
        "openingContinue": {"name1": "continue1.png", "name2": "continue2.png"},
        "openingSound": {"name": "se.ogg", "volume": 0.5},
        "linkingList": [{"(A)": {"main": "chara.png", "back": "chara_back.png"}}],
    }


BASE_TEXT = (
    "(A)「こんにちは」\n"
    '<event name=image file="bg.jpg" x=0 y=0 put>\n'
    "<event name=image file='chara.png' remove>\r\n"
    '<event name=image changefrom=chara.png changeto="chara_back.png">\n'
    "<event name=image removeall>\n"
    '<event name=sound file="se.ogg" volume=0.5 play>\n'
    '<event name=bgm file="bgm.mp3" volume=0.5 play>\n'
    '<event name=dice skill="(A) 目星" result=10 x=1 y=2>\n'
    "<event name=skip pause=1>\n"
)


def make_cassette(
    root: Path,
    conf: dict[str, Any] | None = None,
    maintexts: dict[str, bytes] | None = None,
    name: str = NAME,
) -> Path:
    """検証対象のカセットを tmp に作ります。"""
    conf = base_conf() if conf is None else conf
    cassette = root / name
    for sub in ("config", "maintext", "image", "sound", "other"):
        (cassette / sub).mkdir(parents=True)
    body = "".join(f"    {key} = {value!r}\n" for key, value in conf.items())
    (cassette / "config" / "DialogFrameConfig.py").write_text(
        "class Conf:\n" + body, encoding="utf-8"
    )
    if maintexts is None:
        maintexts = {"main.txt": BASE_TEXT.encode()}
    for file_name, data in maintexts.items():
        (cassette / "maintext" / file_name).write_bytes(data)
    for image in (
        "bg.jpg",
        "chara.png",
        "chara_back.png",
        "start1.png",
        "start2.png",
        "continue1.png",
        "continue2.png",
    ):
        (cassette / "image" / image).write_bytes(b"")
    for sound in ("se.ogg", "bgm.mp3"):
        (cassette / "sound" / sound).write_bytes(b"")
    for other in ("font.ttf", "icon.png"):
        (cassette / "other" / other).write_bytes(b"")
    return cassette


def errors_with(tmp_path: Path, **changes: Any) -> list[str]:
    conf = base_conf()
    conf.update(changes)
    return validate_cassette(make_cassette(tmp_path, conf))


def test_valid_cassette_has_no_errors(tmp_path: Path) -> None:
    assert validate_cassette(make_cassette(tmp_path)) == []


def test_cassette_name_must_match_directory(tmp_path: Path) -> None:
    errors = errors_with(tmp_path, cassette="cassette-other")
    assert len(errors) == 1
    assert "cassette" in errors[0]


def test_maintext_name_must_match_case(tmp_path: Path) -> None:
    cassette = make_cassette(tmp_path, maintexts={"MAIN.txt": BASE_TEXT.encode()})
    errors = validate_cassette(cassette)
    assert len(errors) == 1
    assert "maintext/main.txt" in errors[0]


def test_maintext_list_requires_same_number_of_start_buttons(tmp_path: Path) -> None:
    conf = base_conf()
    conf["maintextName"] = ["a.txt", "b.txt"]
    conf["openingStartList"] = [{"name1": "start1.png", "name2": "start2.png"}]
    cassette = make_cassette(
        tmp_path, conf, {"a.txt": BASE_TEXT.encode(), "b.txt": BASE_TEXT.encode()}
    )
    errors = validate_cassette(cassette)
    assert len(errors) == 1
    assert "openingStartList" in errors[0]


def test_maintext_list_checks_start_button_images(tmp_path: Path) -> None:
    conf = base_conf()
    conf["maintextName"] = ["a.txt"]
    conf["openingStartList"] = [{"name1": "start1.png", "name2": "missing.png"}]
    errors = validate_cassette(make_cassette(tmp_path, conf, {"a.txt": BASE_TEXT.encode()}))
    assert len(errors) == 1
    assert "missing.png" in errors[0]


def test_registered_image_must_exist(tmp_path: Path) -> None:
    conf = base_conf()
    conf["imageConf"].append({"name": "missing.png", "trans": False})
    errors = validate_cassette(make_cassette(tmp_path, conf))
    assert len(errors) == 1
    assert "image/missing.png" in errors[0]


def test_trans_must_be_false_or_coordinate(tmp_path: Path) -> None:
    conf = base_conf()
    conf["imageConf"][0]["trans"] = True
    errors = validate_cassette(make_cassette(tmp_path, conf))
    assert len(errors) == 1
    assert "trans" in errors[0]


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("imageOpenName", "missing.png"),
        ("openingBackGroundImage", "missing.png"),
        ("openingStart", {"name1": "missing.png", "name2": "start2.png"}),
        ("openingContinue", {"name1": "continue1.png", "name2": "missing.png"}),
        ("linkingList", [{"(A)": {"main": "chara.png", "back": "missing.png"}}]),
    ],
)
def test_image_references_must_be_registered(tmp_path: Path, key: str, value: Any) -> None:
    errors = errors_with(tmp_path, **{key: value})
    assert len(errors) == 1
    assert key in errors[0]
    assert "missing.png" in errors[0]


@pytest.mark.parametrize(
    ("key", "value"),
    [
        ("soundTurnPage", "bgm.mp3"),
        ("openingSound", {"name": "bgm.mp3", "volume": 0.5}),
        ("openingBGM", {"name": "se.ogg", "volume": 0.5}),
    ],
)
def test_sound_references_must_be_registered(tmp_path: Path, key: str, value: Any) -> None:
    errors = errors_with(tmp_path, **{key: value})
    assert len(errors) == 1
    assert key in errors[0]


@pytest.mark.parametrize(
    ("key", "path"),
    [("seConf", "sound/missing.ogg"), ("bgmConf", "sound/missing.ogg")],
)
def test_registered_sound_must_exist(tmp_path: Path, key: str, path: str) -> None:
    conf = base_conf()
    conf[key].append({"name": "missing.ogg"})
    errors = validate_cassette(make_cassette(tmp_path, conf))
    assert len(errors) == 1
    assert path in errors[0]


@pytest.mark.parametrize("key", ["dialogFont", "dialogIcon"])
def test_other_files_must_exist(tmp_path: Path, key: str) -> None:
    errors = errors_with(tmp_path, **{key: "missing.bin"})
    assert len(errors) == 1
    assert "other/missing.bin" in errors[0]


def test_missing_required_key_is_reported(tmp_path: Path) -> None:
    conf = base_conf()
    del conf["seConf"]
    errors = validate_cassette(make_cassette(tmp_path, conf))
    assert errors == [f"{NAME}: config: 必須項目 seConf がありません"]


@pytest.mark.parametrize(
    ("line", "expected"),
    [
        ('<event name=image file="missing.png" put>', "imageConf"),
        ("<event name=image file=missing.png x=1 y=2>", "imageConf"),
        ("<event name=image file='missing.png' remove>", "imageConf"),
        ('<event name=image changefrom="chara.png" changeto="missing.png">', "imageConf"),
        ('<event name=sound file="missing.png" volume=0.5 play>', "seConf"),
        ('<event name=bgm file="se.ogg" volume=0.5 play>', "bgmConf"),
    ],
)
def test_event_references_must_be_registered(tmp_path: Path, line: str, expected: str) -> None:
    text = BASE_TEXT + "(A)「非公開のせりふ」\n" + line + "\n"
    errors = validate_cassette(make_cassette(tmp_path, maintexts={"main.txt": text.encode()}))
    assert len(errors) == 1
    assert "maintext/main.txt:11" in errors[0]
    assert expected in errors[0]
    assert "非公開のせりふ" not in errors[0]


def test_maintext_must_be_utf8(tmp_path: Path) -> None:
    cassette = make_cassette(tmp_path, maintexts={"main.txt": "本文".encode("cp932")})
    errors = validate_cassette(cassette)
    assert len(errors) == 1
    assert "UTF-8" in errors[0]


def test_config_is_not_executed(tmp_path: Path) -> None:
    cassette = make_cassette(tmp_path)
    marker = tmp_path / "executed"
    config = cassette / "config" / "DialogFrameConfig.py"
    config.write_text(
        config.read_text(encoding="utf-8") + f"    hook = open({str(marker)!r}, 'w')\n",
        encoding="utf-8",
    )
    errors = validate_cassette(cassette)
    assert not marker.exists()
    assert errors == [f"{NAME}: config: hook がリテラルではありません"]


def test_config_syntax_error_is_reported(tmp_path: Path) -> None:
    cassette = make_cassette(tmp_path)
    (cassette / "config" / "DialogFrameConfig.py").write_text("class Conf:\n    x = (\n")
    errors = validate_cassette(cassette)
    assert len(errors) == 1
    assert "構文エラー" in errors[0]


def test_config_must_be_single_file(tmp_path: Path) -> None:
    cassette = make_cassette(tmp_path)
    (cassette / "config" / "Other.py").write_text("class Conf:\n    pass\n")
    assert validate_cassette(cassette) == [
        f"{NAME}: config: config/*.py がひとつではありません (2 件)"
    ]


def test_main_validates_all_cassettes(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    make_cassette(tmp_path)
    conf = base_conf()
    conf["cassette"] = "cassette-broken"
    conf["dialogFont"] = "missing.ttf"
    make_cassette(tmp_path, conf, name="cassette-broken")

    assert main(["--root", str(tmp_path)]) == 1
    out = capsys.readouterr().out
    assert f"{NAME}: OK" in out
    assert "cassette-broken: other/missing.ttf" in out


def test_main_validates_named_cassette(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    make_cassette(tmp_path)
    assert main(["--root", str(tmp_path), NAME]) == 0
    assert capsys.readouterr().out == f"{NAME}: OK\n"


def test_main_rejects_unknown_cassette(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    make_cassette(tmp_path)
    assert main(["--root", str(tmp_path), "cassette-none"]) == 1
    assert "cassette-none: カセットがありません" in capsys.readouterr().out


def test_main_fails_without_cassettes(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["--root", str(tmp_path)]) == 1
    assert "カセットがありません" in capsys.readouterr().out


def test_repository_cassettes_are_valid() -> None:
    cassettes = sorted(REPO_ROOT.glob("cassette-*"))
    assert len(cassettes) == 4
    assert [error for c in cassettes for error in validate_cassette(c)] == []
