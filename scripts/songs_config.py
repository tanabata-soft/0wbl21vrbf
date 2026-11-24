"""作品の曲設定（NK-S007）。

単位D（生成器一本化）: 生成器本体の正はテンプレート repo
（mmishina-art/digitalcd-engine）の scripts/chartgen/ パッケージ1か所。
作品側はこの SONGS メタデータと歌詞入力（src/game/data/lyrics.json）だけを
持ち、scripts/generate-charts.py（入口ブートストラップ）がテンプレートの
chartgen を参照して生成する。曲を足すときはここに1曲分を足す。
各キーの意味はテンプレート scripts/chartgen/config.py のコメント参照。
"""

SONGS = {
    # NK-S007『SHIFT AWARD 2026 応援歌』の収録曲。音源は src/game/assets/track0N.mp3
    # （制作入口で用意した唯一の正規音源 MP3 192kbps。CD 側プレイヤーも同じ音源を共有する）。
    # FEVER（サビ）区間は、歌詞（src/album/sync.ts）の反復・掛け声ブロックから決める:
    # ブロックの先頭行の開始秒を開始、末尾行の歌唱が終わる頃を終了とする
    # （NK-S003 での決め方）。サビは歌に合わせて主レイヤーを vocal にする
    # （NK-S003 のオーナー指示）。
    "kassai": {
        "title": "黒い画面の喝采",
        "audio": "src/game/assets/track01.mp3",
        # 掛け声ブロック: 47.6〜59.7 / 96.0〜107.6 / 終盤 143.8〜156.0（各末尾行の終わりまで）
        "fever": [[48.0, 64.0], [96.0, 117.0], [144.0, 166.0]],
        "chart_v5": True,
        "chorus_layer": "vocal",
        "chorus_bonus": 0.5,
        "flick": True,
        "flick_budget": {"easy": 6, "normal": 6, "hard": 9},
    },
    "jidai": {
        "title": "時代を動かせ",
        "audio": "src/game/assets/track02.mp3",
        # サビは同一ブロックの反復: 38.3〜60.5 / 102.2〜124.5（各末尾行の終わりまで）
        "fever": [[38.0, 64.0], [102.0, 128.0]],
        "chart_v5": True,
        "chorus_layer": "vocal",
        "chorus_bonus": 0.5,
        "flick": True,
        "flick_budget": {"easy": 9, "normal": 12, "hard": 17},
    },
}
