# B-team Report App

## 📌 概要
日報・引継ぎ・障害/問い合わせのレポートを  
登録・検索・閲覧するためのデスクトップアプリです。

- Python + Tkinter で画面構築
- MySQL を利用したデータ管理
- キーワード検索 + 種別検索に対応

---

## 🖥️ 画面構成

### 🔍 検索画面
- キーワード入力
- 種別チェック
- 検索 / 新規登録遷移

### 📄 検索結果画面
- 検索結果表示
- 詳細画面遷移

### 📑 詳細画面
- レポート内容表示
- Slack / Jira / Notion 形式コピー

### ➕ 新規登録画面
以下の三種類の登録を行う
- 日報：Standup
- 引継ぎ：Handover
- 障害/問い合わせ：Incident

```
src/
├─ main.py                 # エントリーポイント
├─ app.py                  # アプリ管理
├─ utils.py                # 共通処理
└─ screens/
   ├─ SearchScreen.py
   ├─ SearchResultScreen.py
   ├─ DetailScreen.py
   ├─ DBAccess.py
   ├─ NewRegistrationStandup.py
   ├─ NewRegistrationHandover.py
   └─ NewRegistrationIncident.py
```

## 🗄️ DBアクセス
DB処理は `DBAccess.py` に集約。

- search() : 検索
- get() : 詳細取得
- register() : 登録

---

## 🔎 検索仕様

### キーワード
- 半角スペース区切り
- OR検索

例:
API 設計 障害

### 種別
- standup
- handover
- incident
※ 全選択 / 無選択は同一扱い（全件対象）

---

## 🚀 起動方法
### 起動
python main.py

---
## ⚠️ 注意事項
- MySQL がローカル起動していること
- DB設定は `DBAccess.py` 内
---
## 🧪 開発目的
- Tkinter GUI開発学習
- Python DBアクセス理解
- チーム開発練習