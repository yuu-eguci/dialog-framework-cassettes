DialogFrame Cassettes
===

対話劇作成フレームワーク DialogFrame のカセット集です。フレームワーク本体は別リポジトリで、このリポジトリには含みません。

## カセットの構成

`cassette-*` ディレクトリひとつがカセットひとつです。

| パス | 内容 |
| --- | --- |
| `config/*.py` | 設定クラス `Conf` です。ファイルはひとつだけ置きます |
| `maintext/` | 本文テキスト (UTF-8) です |
| `image/` | 画像です。 `image/その他素材/` は編集用の元素材で、 config からは参照しません |
| `sound/` | 効果音と BGM です |
| `other/` | フォント ・アイコン ・セーブ DB (`save.sqlite3` 、初期状態の `(新品)save.sqlite3`) です |
| `log/` | 実行ログの出力先です。中身は Git の管理対象外です |

### config の参照ルール

- `cassette` はディレクトリ名と同じにします。
- `maintextName` は `maintext/` 内のファイル名です。複数の本文から選ぶ場合はリストにし、 `openingStartList` に同じ数の「はじめから」ボタンを書きます。ひとつの場合は `openingStart` と `openingContinue` を使います。
- `imageConf` には `image/` 内の画像を登録します。 `trans` は `False` か、透明色にする座標 `(x, y)` です。
- `imageOpenName` ・ `openingBackGroundImage` ・オープニングのボタン画像 ・ `linkingList` の `main` と `back` は、 `imageConf` に登録した画像を指定します。
- `seConf` と `bgmConf` には `sound/` 内のファイルを登録します。 `soundTurnPage` と `openingSound` は `seConf` 、 `openingBGM` は `bgmConf` に登録したファイルを指定します。
- `dialogFont` と `dialogIcon` は `other/` 内のファイルです。
- ファイル名は大文字小文字まで一致させます。

### 本文の event タグ

| タグ | 参照先 |
| --- | --- |
| `<event name=image file=... x=... y=...>` ほか `put` ・ `remove` 付き | `imageConf` |
| `<event name=image changefrom=... changeto=...>` | `imageConf` |
| `<event name=image removeall>` | なし |
| `<event name=sound file=... volume=... play>` | `seConf` |
| `<event name=bgm file=... volume=... play>` | `bgmConf` |
| `<event name=dice skill=... result=... x=... y=...>` | なし (`diceDic` にある技能は成否を表示します) |
| `<event name=skip>` ほか `back` ・ `pause` 付き | なし |

## 検証

Docker だけで実行できます。 config は実行せずに読み込み、上記の参照ルールと本文の event タグの参照先を検証します。エラーにはファイル名 ・行番号 ・素材名だけを表示し、本文の内容は表示しません。

```bash
# 全カセットを検証します
docker compose run --rm --build validate

# 特定のカセットだけ検証します
docker compose run --rm --build validate cassette-matetrpg1mary

# lint (ruff) ・型チェック (mypy) ・テスト (pytest) を実行します
docker compose run --rm --build check

# 後片付けをします
docker compose down --rmi all
```

GitHub Actions でも同じ `check` と `validate` を実行します。

## ライセンス

各カセットの `other/VL-Gothic-Regular.ttf` は VL Gothic 20141206 (Version 2.120) です。ライセンス文は上流配布物から無変更で `licenses/VL-Gothic/` に収録しています。

## 開発用ファイル

| パス | 内容 |
| --- | --- |
| `tools/validate_cassettes.py` | 検証スクリプトです。標準ライブラリのみで動きます |
| `tests/` | 検証スクリプトのテストです |
| `requirements-dev.in` | `check` で使う ruff ・ mypy ・ pytest の版指定です |
| `requirements-dev.txt` | `requirements-dev.in` から生成したハッシュ付きの固定版です |

`requirements-dev.in` を変更したら、次のコマンドで `requirements-dev.txt` を再生成します。

```bash
docker run --rm -v "$PWD:/w" -w /w python:3.15.2-slim-trixie sh -c 'pip install uv==0.13.9 && uv pip compile requirements-dev.in --universal --generate-hashes --python-version 3.15 --no-header -o requirements-dev.txt'
```
