
import tkinter as tk

# 検索
class SearchScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="検索").pack()
        tk.Button(self, text="検索結果",
                  command=lambda: master.show_frame("SearchResultScreen")).pack(expand=True)
        tk.Button(self, text="新規登録 Standup",
                  command=lambda: master.show_frame("NewRegistrationStandup")).pack(expand=True)
        tk.Button(self, text="新規登録 Handover",
                  command=lambda: master.show_frame("NewRegistrationHandover")).pack(expand=True)
        tk.Button(self, text="新規登録 Incident",
                  command=lambda: master.show_frame("NewRegistrationIncident")).pack(expand=True)
