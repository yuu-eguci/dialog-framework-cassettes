# coding: utf-8

class Conf:
    """DialogFrameの設定クラス。"""

    # 使うカセット。フォルダの名前。cassetteって付いてるのはただの趣味だからなんでもよい。
    cassette = 'cassette-matetrpg1mary'
    # メインテキストの名前
    maintextName = 'matetrpg壁に耳あり.txt'

    # 画像はimageフォルダに入れること。
    #     name ファイル名
    #     trans 透明色にしたい色の座標 もともと透明のPNGならFalseでいいよ親切機能だから
    imageConf = [
        {
            'name': 'bg_bed.jpg',
            'trans': False,
        },
        {
            'name': 'bg_skype.jpg',
            'trans': False,
        },
        {
            'name': 'bg_tatami.jpg',
            'trans': False,
        },
        {
            'name': 'dialogbox.png',
            'trans': False,
        },
        {
            'name': 'diceframe.png',
            'trans': False,
        },
        {
            'name': 'm_reading.png',
            'trans': False,
        },
        {
            'name': 'm_reading2.png',
            'trans': False,
        },
        {
            'name': 'mob_oriduru.png',
            'trans': False,
        },
        {
            'name': 'op_continue1.png',
            'trans': False,
        },
        {
            'name': 'op_continue2.png',
            'trans': False,
        },
        {
            'name': 'op_start1.png',
            'trans': False,
        },
        {
            'name': 'op_start2.png',
            'trans': False,
        },
        {
            'name': 'sheet.png',
            'trans': False,
        },
        {
            'name': 'w_futon.png',
            'trans': False,
        },
        {
            'name': 'w_futon2.png',
            'trans': False,
        },
        {
            'name': 'w_kimono.png',
            'trans': False,
        },
        {
            'name': 'w_kimono2.png',
            'trans': False,
        },
        {
            'name': 'w_pajamas.png',
            'trans': False,
        },
        {
            'name': 'w_pajamas2.png',
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
    dialogTitle = 'MATETRPG 壁に耳あり'
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

    # 発言者と立ち絵の関連付け
    #     AさんのダイアログではAさんの立ち絵が明るくなり、そうでなければ暗くなる、ってのが自動で出来る。
    #     左側にはキー、右側のmainに明るいほう、backに暗いほうの画像名を書いてね。
    #     この自動操作は<event name=image>タグでその画像が表示状態のときのみ発生する
    linkingList = [
        {'(KP)': {'main':'m_reading.png', 'back':'m_reading2.png'}},
        {'(エル)': {'main':'w_futon.png', 'back':'w_futon2.png'}},
        {'(エル)': {'main':'w_kimono.png', 'back':'w_kimono2.png'}},
        {'(エル)': {'main':'w_pajamas.png', 'back':'w_pajamas2.png'}},
    ]

    # ダイスロールで、自動で成功失敗を表示するための設定
    # ここに記述した技能に関しては成功失敗クリファンが出る
    diceDic = {
        '隠れる': 60,
        '聞き耳': 75,
        '登攀': 63,
        '目星': 75,
        '考古学': 51,
        '電子工学': 50,
        '博物学': 50,
        '変装': 99,
        '芸術(ポケモン)': 69,
        'アイディア': 70,
        '幸運': 60,
        '知識': 60,
        'SANチェック': 60,
        'DEX*5': 55,
        'こぶし': 50,
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

