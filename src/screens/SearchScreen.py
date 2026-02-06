
import tkinter as tk
from tkinter import messagebox, scrolledtext
from screens.DBAccess import DBAccess

# 検索
class SearchScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        frame = tk.Frame(self)
        frame.pack(side="top", fill="x", padx=10, pady=5)
        #チェックボックス用変数
        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()
        tk.Label(frame, text=f"検索", font=("Arial", 14, "bold")).pack(side="left")
        #検索ボタン押下時コマンド呼び出し
        tk.Button(frame, text="検索", font=("Arial", 12), padx=8, pady=4,
                  command=self.on_search).pack(side="right", padx=5)
        #新規登録ボタン押下時コマンド呼び出し
        tk.Button(frame, text="新規登録", font=("Arial", 12), padx=8, pady=4,
                  command=self.on_newreg).pack(side="right", padx=5)

        #検索条件用テキストボックス及びエンター入力受付
        self.text = tk.Text(self, font=("Arial", 14), wrap="word", height=1)
        self.text.pack(anchor="w", padx=10, pady=5)
        self.text.insert("1.0", "" )
        self.text.bind("<Return>", self.on_search)

        #チェックボックス管理
        tk.Checkbutton(self,text="日報", font=("Arial", 12), variable=self.var1, padx=8, pady=4).pack(anchor="w", padx=5)
        tk.Checkbutton(self,text="引継ぎ", font=("Arial", 12), variable=self.var2, padx=8, pady=4).pack(anchor="w", padx=5)
        tk.Checkbutton(self,text="障害/問い合わせ", font=("Arial", 12), variable=self.var3, padx=8, pady=4).pack(anchor="w", padx=5)

    #検索用関数
    def on_search(self, event=None):
        value = self.text.get("1.0", "end-1c")
        searchwords = value.split()
        v1 = self.var1.get()
        v2 = self.var2.get()
        v3 = self.var3.get()
        types = []

        #種別選択
        if v1:
            types.append("standup")
        if v2:
            types.append("handover")
        if v3:
            types.append("incident")
        #全て選択または無選択を等しい処理とする
        if len(types) in (0, 3) :
            types = []

        where_clauses = []
        params = []

        if len(searchwords) >= 1:
            keywords = []
            for searchword in searchwords:
                keywords.append("body LIKE %s")
                params.append(f"%{searchword}%")
            where_clauses.append("(" + " OR ".join(keywords) + ")")

        # type検索
        if len(types) >= 1:
            type_conditions = []
            for type in types:
                type_conditions.append("type = %s")
                params.append(type)
            where_clauses.append("(" + " OR ".join(type_conditions) + ")")

        # SQL生成
        sql = "SELECT * FROM records"

        if where_clauses:
            sql += " WHERE " + " AND ".join(where_clauses)

        print(sql)
        print(params)

        # self.master.frames["SearchResultScreen"].set_search(sql, params)
        self.master.search_result = DBAccess().search(sql ,params)
        self.master.show_frame("SearchResultScreen")
        self.master.focus_set() 
        return "break" 

    #新規登録画面呼び出し用関数
    def on_newreg(self, event=None): 
        v1 = self.var1.get()
        v2 = self.var2.get()
        v3 = self.var3.get()
        if v1 and not v2 and not v3:
#            print("日報")
            self.master.show_frame("NewRegistrationStandup")
        elif not v1 and v2 and not v3:
#            print("引継ぎ")
            self.master.show_frame("NewRegistrationHandover")
        elif not v1 and not v2 and v3:
#            print("障害/問い合わせ")
            self.master.show_frame("NewRegistrationIncident")
        else :
#           print("新規登録の際はチェックボックス一つのみにチェックを入れてボタンを押下してください。")
            messagebox.showinfo('注意', '新規登録の際はチェックボックス一つのみにチェックを入れてボタンを押下してください。')

