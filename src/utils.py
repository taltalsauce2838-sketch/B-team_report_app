def cnv_txt(txt):
    text_mapping = {
        # recode
        "type": "種類",
        "title": "タイトル",
        "body": "内容",
        "meta_json": "詳細",
        "created_at": "作成日時",
        "updated_at": "作成日時",
        # type
        "standup": "日報",
        "handover": "引継ぎ",
        "incident": "障害/問い合わせ",
        # JSON
        "date": "日付",
        "done": "昨日やったこと",
        "today": "今日やること",
        "blocker": "困りごと",
        "ticket": "チケット番号",
        "context": "背景",
        "current": "現状",
        "next": "次アクション",
        "notes": "注意点",
        "links": "参考リンク",
        "summary": "現象",
        "impact": "影響範囲",
        "env": "環境",
        "repro_steps": "再現手順",
        "logs_checked": "確認済みログ",
        "hypothesis": "仮説",
    }
    return text_mapping.get(txt, txt)
