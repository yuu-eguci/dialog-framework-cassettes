"""同梱フォントのライセンス表示を確認するテストです。"""

from __future__ import annotations

import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LICENSE_DIR = REPO_ROOT / "licenses" / "VL-Gothic"
# VLGothic-20141206.tar.xz に含まれるファイルの SHA-256 です。
VL_GOTHIC_FONT_SHA256 = "f862be2fb640f02f7bbf8ab000c867eb020e29bc1faf0e08c6bbae328b5b9bf8"
VL_GOTHIC_LICENSE_SHA256 = {
    "LICENSE": "a3789bc523653f59c24f34cff4f0f227faeedf6d6fd952b61dacf6dd5f06282f",
    "LICENSE.en": "da57434c3dd14839fc06bb9d226817a1829fbf5c229c6c640a085c2600a67d5d",
    "LICENSE_E.mplus": "627446730facc8227f815de9751838ad0433d6870ff45f3d3024b25c3838b826",
    "LICENSE_J.mplus": "dd010309f51c2306e7dfc208d3f9830ed49b71f358dcc6adecd1af398af9feee",
    "README.sazanami": "a74b381afb202e5db3d481dab992243e62bdb70a16d3987d2480f25ad463fd3c",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_bundled_fonts_are_vl_gothic_20141206() -> None:
    fonts = sorted(REPO_ROOT.glob("cassette-*/other/*.ttf"))
    assert [font.name for font in fonts] == ["VL-Gothic-Regular.ttf"] * 4
    assert {sha256(font) for font in fonts} == {VL_GOTHIC_FONT_SHA256}


def test_vl_gothic_license_files_are_unchanged() -> None:
    assert {path.name: sha256(path) for path in LICENSE_DIR.iterdir()} == VL_GOTHIC_LICENSE_SHA256
