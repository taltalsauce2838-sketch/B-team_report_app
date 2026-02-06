
import tkinter as tk
from screens.DBAccess import DBAccess

# 検索結果
class SearchResultScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="検索結果").pack()
        tk.Button(self,text="検索",
                  command=lambda: master.show_frame("SearchScreen")).pack()
        tk.Button(self, text="詳細",
                  command=lambda: master.show_frame("DetailScreen")).pack(expand=True)

        #
        result = self.master.search_result
    def set_search(self, sql ,params):
        db = DBAccess().search(sql ,params)
        print(db)
        


