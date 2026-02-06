
import tkinter as tk

# 新規登録 Standup
class NewRegistrationStandup(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="新規登録 Standup").pack()
        
        # 1. 項目名の定義（データ）
        fields = ["種別", "現象", "影響範囲", "環境", "再現手順", "確認済みログ", "仮説"]
        
        # 2. 内容を保持するための変数（辞書）
        self.entries = {}

        # 3. ループによる一括生成
        for field in fields:
            # ラベルの配置
            tk.Label(self, text=field).pack(anchor="w", padx=10)
            
            # Entryの生成と辞書への格納
            entry = tk.Entry(self)
            entry.pack(fill="x", padx=10, pady=(0, 5))
            
            # 項目名をキーにしてインスタンスを記憶
            self.entries[field] = entry

       
        #検索に遷移するボタン
        tk.Button(self, text="検索",
                  command=lambda: master.show_frame("SearchScreen")).place(relx=1.0, rely=0.0,anchor="ne",x=-10,y=10)

        #登録を実行するボタン
        tk.Button(self, text="登録",
                  command=lambda: master.show_frame("SearchScreen")).place(relx=1.0, rely=1.0,anchor="se",x=-10,y=-10)
        #中身が大嘘なので修正