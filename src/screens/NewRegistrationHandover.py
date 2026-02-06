
import tkinter as tk
from screens.DBAccess import DBAccess
import json
from datetime import datetime

# 新規登録 Handover
class NewRegistrationHandover(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="新規登録 Handover").pack()
        
         
        # 1. 項目名の定義（データ）
        fields = ["種別", "日付", "昨日", "今日", "困りごと", "チケット番号"]
        
        # 2. 内容を保持するための変数（辞書）
        self.entries = {}

        # 3. ループによる一括生成
        for field in fields:
            if field=="種別":
                entry = "handover"
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
        

        #検索に遷移するボタン
        tk.Button(self, text="検索",
                  command=lambda: master.show_frame("SearchScreen")).place(relx=1.0, rely=0.0,anchor="ne",x=-10,y=10)
        # 登録ボタン：ここから「self.execute_registration」を呼び出す
        tk.Button(self, text="登録",
                  command=self.execute_registration).place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)
    
    def execute_registration(self):
        # 1. 最新の入力を取得
        v = {k: (val if k == "種別" else val.get()) for k, val in self.entries.items()}

        # 2. DB用の辞書をその場で作成（ローカル変数で良い）
        entry_DB = {
        "type": v["種別"],
        "title": "",  # VARCHAR(20)の制限に合わせてスライス
        "body": f"日付:{v['日付']} 昨日:{v['昨日']} 今日:{v['今日']} 困りごと:{v['困りごと']}"[:100],  # {}ではなくf-stringで文字列化し、100文字制限
        "meta_json": json.dumps(v, ensure_ascii=False),  # 集合{}ではなくjson.dumpsで文字列化
        "created_at": datetime.now(),
        "updated_at": datetime.now()
        }
    

        # 3. DBアクセス実行
        db = DBAccess()
        db.register(entry_DB)
        
        print("最新の入力内容で登録を試みました:", entry_DB)