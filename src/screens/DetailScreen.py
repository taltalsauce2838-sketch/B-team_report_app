import tkinter as tk

# 詳細
class DetailScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="詳細").pack()
        tk.Button(self, text="検索",
                  command=lambda: master.show_frame("SearchScreen")).pack(expand=True)
        tk.Button(self, text="検索結果",
                  command=lambda: master.show_frame("SearchResultScreen")).pack(expand=True)