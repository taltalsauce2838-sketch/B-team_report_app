
import tkinter as tk

# 新規登録 Incident
class NewRegistrationIncident(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="新規登録 Incident").pack()
        tk.Button(self, text="検索",
                  command=lambda: master.show_frame("SearchScreen")).pack(expand=True)
