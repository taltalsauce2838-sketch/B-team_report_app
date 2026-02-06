
import tkinter as tk
from screens.DBAccess import DBAccess
import json
from datetime import datetime

# 新規登録 Incident
class NewRegistrationIncident(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="新規登録 Incident").pack()

        
        # 1. 項目名の定義（データ）
        fields = ["種別", "タイトル", "背景", "現状", "次アクション", "注意点", "参考リンク"]
        
        # 2. 内容を保持するための変数（辞書）
        self.entries = {}

        # 3. 入力フォームの生成
        for field in fields:
            # ラベルの配置
           
            if field=="種別":
                entry = "incident"
            else:
                # Entryの生成と辞書への格納
                tk.Label(self, text=field).pack(anchor="w", padx=10)
                entry = tk.Entry(self)
                entry.pack(fill="x", padx=10, pady=(0, 5))
                
            # 項目名をキーにしてインスタンスを記憶
            self.entries[field] = entry


       #検索に遷移するボタン
        tk.Button(self, text="検索",
                  command=lambda: master.show_frame("SearchScreen")).place(relx=1.0, rely=0.0,anchor="ne",x=-10,y=10)
        tk.Button(self, text="登録",
                  command=self.execute_registration).place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
       
    
    def execute_registration(self):
        # 1. 最新の入力を取得
        v = {k: (val if k == "種別" else val.get()) for k, val in self.entries.items()}

        # 2. DB用の辞書をその場で作成（ローカル変数で良い）
        entry_DB = {
            "type": v["種別"],
            "title": v["タイトル"][:20],  # VARCHAR(20)の制限に合わせてスライス
            "body": f"背景:{v['背景']} 現状:{v['現状']} 次アクション:{v['次アクション']} 注意点:{v['注意点']}"[:100],  # {}ではなくf-stringで文字列化し、100文字制限
            "meta_json": json.dumps(v, ensure_ascii=False),  # 集合{}ではなくjson.dumpsで文字列化
            "created_at": datetime.now(),
            "updated_at": datetime.now()
            }

        # 3. DBアクセス実行
        db = DBAccess()
        db.register(entry_DB)
        
        print("最新の入力内容で登録を試みました:", entry_DB)
