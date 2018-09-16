# coding: utf-8

class Conf:
    """DialogFrameの設定クラス。"""

    # 使うカセット。フォルダの名前。cassetteって付いてるのはただの趣味だからなんでもよい。
    cassette = 'cassette-matetrpg3kataware'
    # メインテキストの名前
    maintextName = [
        'matetrpg3-1.txt',
        'matetrpg3-2.txt',
        'matetrpg3-3.txt',
    ]

    # 画像はimageフォルダに入れること。
    #     name ファイル名
    #     trans 透明色にしたい色の座標 もともと透明のPNGならFalseでいいよ親切機能だから
    imageConf = [
        {
            'name': 'bg_skype.jpg',
            'trans': False,
        },
        {
            'name': 'bg_country.jpg',
            'trans': False,
        },
        {
            'name': 'bg_trees.jpg',
            'trans': False,
        },
        {
            'name': 'bg_ryokan.jpg',
            'trans': False,
        },
        { # [50, 175]
            'name': 'chara_gm.png',
            'trans': False,
        },
        {
            'name': 'chara_gm_back.png',
            'trans': False,
        },
        { # [382, 114]
            'name': 'chara_inu.png',
            'trans': False,
        },
        {
            'name': 'chara_inu_back.png',
            'trans': False,
        },
        { # [499, 127]
            'name': 'chara_kabu.png',
            'trans': False,
        },
        {
            'name': 'chara_kabu_back.png',
            'trans': False,
        },
        {
            'name': 'chara_kabu_kabu.png',
            'trans': False,
        },
        {
            'name': 'chara_kabu_kabu_back.png',
            'trans': False,
        },
        {
            'name': 'chara_kabu_ribbon.png',
            'trans': False,
        },
        {
            'name': 'chara_kabu_ribbon_back.png',
            'trans': False,
        },
        { # [20, 320]
            'name': 'dialogbox.png',
            'trans': False,
        },
        { # [145, 60]
            'name': 'material_circle.png',
            'trans': False,
        },
        { # [195, 100]
            'name': 'mob_female.png',
            'trans': False,
        },
        { # [200, 95]
            'name': 'mob_male.png',
            'trans': False,
        },
        { # [185, 95]
            'name': 'mob_monster.png',
            'trans': False,
        },
        { # [195, 95]
            'name': 'mob_nae.png',
            'trans': False,
        },
        { # [200, 95]
            'name': 'mob_touno.png',
            'trans': False,
        },
        {
            'name': 'diceframe.png',
            'trans': False,
        },
        {
            'name': 'blank1.png',
            'trans': False,
        },
        {
            'name': 'blank2.png',
            'trans': False,
        },
        {
            'name': 'blank3.png',
            'trans': False,
        },
        {
            'name': 'blank4.png',
            'trans': False,
        },
        {
            'name': 'blank5.png',
            'trans': False,
        },
        {
            'name': 'blank6.png',
            'trans': False,
        },
        {
            'name': 'sheet.png',
            'trans': False,
        },
        {
            'name': 'sheet_inu.png',
            'trans': False,
        },
        {
            'name': 'sheet_kabu.png',
            'trans': False,
        },
        {
            'name': 'map0.jpg',
            'trans': False,
        },
        {
            'name': 'map1.jpg',
            'trans': False,
        },
        {
            'name': 'map2.jpg',
            'trans': False,
        },
        {
            'name': 'op_start1-1.png',
            'trans': False,
        },
        {
            'name': 'op_start1-2.png',
            'trans': False,
        },
        {
            'name': 'op_start2-1.png',
            'trans': False,
        },
        {
            'name': 'op_start2-2.png',
            'trans': False,
        },
        {
            'name': 'op_start3-1.png',
            'trans': False,
        },
        {
            'name': 'op_start3-2.png',
            'trans': False,
        },

    ]

    # 「いつでも画像オープン」に画像を登録
    imageOpenName = 'sheet.png'
    imageOpenXY = [60, 30]

    # SEはsoundフォルダに入れること。
    #     name ファイル名
    seConf = [
        {
            'name': 'ban.ogg',
        },
        {
            'name': 'switch.ogg',
        },
        {
            'name': 'switch2.ogg',
        },
    ]

    # ページ送り時のSE
    soundTurnPage = 'switch2.ogg'

    # BGMはsoundフォルダに入れること。
    #     name ファイル名
    bgmConf = [
        {
            'name': 'cave.mp3',
        },
    ]

    # タイトル
    dialogTitle = 'MATETRPG3 かたわれ 1'
    # フォント。変更する場合はotherフォルダに入れること。
    dialogFont = 'VL-Gothic-Regular.ttf'
    # ダイアログ文字の大きさ
    dialogFontSize = 18
    # ダイアログ文字を表示する座標
    dialogX = 25
    dialogY = 325
    # ダイアログ文字の色
    dialogColor = (255,255,255)

    # オープニングを使うかどうか。TrueかFalse。
    useOpening = True
    # オープニング背景
    openingBackGroundImage = 'bg_skype.jpg'
    # オープニングBGM
    openingBGM = {
        'name': 'cave.mp3',
        'volume': 0.5,
    }

    # maintextNameがリストじゃないとき(使用するmaintextがひとつ)
    # 「はじめから」の画像 
    openingStart = {
        'name1': 'op_start1.png',
        # カーソル合ってるときの画像
        'name2': 'op_start2.png',
        'x': 480,
        'y': 340,
        # カーソル合ってるときどんくらい揺らす?
        'shake': 10,
    }
    # 「つづきから」の画像
    openingContinue = {
        'name1': 'op_continue1.png',
        # カーソル合ってるときの画像
        'name2': 'op_continue2.png',
        'x': 480,
        'y': 400,
        # カーソル合ってるときどんくらい揺らす?
        'shake': 10,
    }
    # スタートするときのSE
    openingSound = {
        'name': 'switch.ogg',
        'volume': 0.5,
    }

    # maintextNameがリストのとき(使用するmaintextが複数)
    openingStartList = [
        # 分岐するmaintextのぶんだけ書くこと
        {
            'name1': 'op_start1-1.png',
            'name2': 'op_start1-2.png',
            'x': 470,
            'y': 220,
            'shake': 10,
        },
        {
            'name1': 'op_start2-1.png',
            'name2': 'op_start2-2.png',
            'x': 470,
            'y': 300,
            'shake': 10,
        },
        {
            'name1': 'op_start3-1.png',
            'name2': 'op_start3-2.png',
            'x': 470,
            'y': 380,
            'shake': 10,
        },
    ]

    # 発言者と立ち絵の関連付け
    #     AさんのダイアログではAさんの立ち絵が明るくなり、そうでなければ暗くなる、ってのが自動で出来る。
    #     左側にはキー、右側のmainに明るいほう、backに暗いほうの画像名を書いてね。
    #     この自動操作は<event name=image>タグでその画像が表示状態のときのみ発生する
    linkingList = [
        {'(GM)':        {'main':'chara_gm.png',          'back':'chara_gm_back.png'}},
        {'(神山犬千代)': {'main':'chara_inu.png',         'back':'chara_inu_back.png'}},
        {'(緑色かぶき)':  {'main':'chara_kabu.png',        'back':'chara_kabu_back.png'}},
        {'(緑色かぶき)':  {'main':'chara_kabu_kabu.png',   'back':'chara_kabu_kabu_back.png'}},
        {'(緑色かぶき)':  {'main':'chara_kabu_ribbon.png', 'back':'chara_kabu_ribbon_back.png'}},
        {'(GM)':        {'main':'material_circle.png',   'back':'blank1.png'}},
        {'(GM)':        {'main':'mob_female.png',        'back':'blank2.png'}},
        {'(GM)':        {'main':'mob_male.png',          'back':'blank3.png'}},
        {'(GM)':        {'main':'mob_monster.png',       'back':'blank4.png'}},
        {'(GM)':        {'main':'mob_nae.png',           'back':'blank5.png'}},
        {'(GM)':        {'main':'mob_touno.png',         'back':'blank6.png'}},
    ]

    # ダイスロールで、自動で成功失敗を表示するための設定
    # ここに記述した技能に関しては成功失敗クリファンが出る
    diceDic = {
        'かぶき SANチェック'      : 60,
        'かぶき アイディア'  : 55,
        'かぶき 幸運'     : 60,
        'かぶき 知識'     : 95,
        'かぶき 隠れる'    : 70,
        'かぶき 聞き耳'    : 85,
        'かぶき 忍び歩き'   : 70,
        'かぶき 目星'     : 75,
        'かぶき 投擲'     : 75,
        'かぶき 説得'     : 65,
        'かぶき 芸術(歌舞伎)': 85,
        'かぶき 変装'     : 81,
        'かぶき DEX対抗': 55,
        'かぶき ショックロール': 55,
        '犬千代 SANチェック'    : 70,
        '犬千代 アイディア'  : 75,
        '犬千代 幸運'     : 70,
        '犬千代 知識'     : 90,
        '犬千代 鍵開け'    : 81,
        '犬千代 隠す'     : 70,
        '犬千代 隠れる'    : 70,
        '犬千代 聞き耳'    : 55,
        '犬千代 追跡'     : 55,
        '犬千代 目星'     : 70,
        '犬千代 回避'     : 82,
        '犬千代 信用'     : 65,
        '犬千代 重機械操作': 89,
        '犬千代 こぶし': 50,
        '犬千代 ショックロール': 50,
        '敵 投擲': 50,
    }
    # ダイスロールアニメで数字が切り替わる数
    diceNum = 30

    # フレームレート。大きくするとゲームループが速くなってCPU負荷がヤバくなる。小さくするとCPUは軽いけど遅くなる。
    # 20~30くらいでどうぞ。
    framerate = 20

    # ヘルプのメッセージ。
    helpConf = {
        # 「ヘルプ:F11」みたいな表示をどこに配置するか。nw,ne,sw,seで指定してね。いらないなら''に。
        'location': 'se',
        # 表示ボックスの色
        'boxColor': (128,128,0),
        'mesColor': (255,255,255),
        # 表示の色
        # ヘルプ内容 一行ずつ書いてね。
        'message': [
            'キーヘルプ',
            'Z:進む',
            'X:ページ戻りモードへ',
            'C:キャラシートを見る',
            '数字1～4:セーブ',
            'F1～F4:ロード',
            'F12:タイトル画面に戻る',
        ],
    }

    # ページ戻りモード
    pageBackMode = {
        # ページ戻りモードの通知内容
        'message': 'ページ戻りモードです。Z:進む X:さらに戻る',
        # 通知ボックスの色
        'boxColor': (72,61,139),
        # 通知文字色
        'mesColor': (255,255,255),
        # 普通タグはスキップするが、以下から始まるタグは無視しない
        'pass': [
            '<event name=dice',
        ],
    }

    # セーブとかロードとか、あとヘルプ表示するとき出るボックスの設定。
    announceConf = {
        # ボックスの色
        'boxColor': (34,139,34),
        # 文字色
        'mesColor': (255,255,255),
    }

    # セーブ、ロード機能を使うかどうか。
    useSave = True

    # キーコンフィグ。
    keyConf = {
        # ページ送りページ戻り
        'turnPage': 'z',
        'backPage': 'x',
        # いつでも画像オープン 俺は主にキャラシオープンに使ってる
        'imageOpen': 'c',
        # セーブ
        'save1': '1',
        'save2': '2',
        'save3': '3',
        'save4': '4',
        # ロード
        'load1': 'f1',
        'load2': 'f2',
        'load3': 'f3',
        'load4': 'f4',
        # ヘルプを見る
        'showHelp': 'f11',
        # スタート画面へ戻る
        'goToStart': 'f12',
    }

    # アイコン。これはotherフォルダに入れること。
    dialogIcon = 'pythongreen32x32.png'

