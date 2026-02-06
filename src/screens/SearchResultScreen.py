import tkinter as tk
from screens.DBAccess import DBAccess
from utils import cnv_txt

# 検索結果画面
class SearchResultScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        #
        self.bgcolor = "#99AABB"
        self.row_height = 40

        
        # 固定ヘッダー
        header_frame = tk.Frame(self)
        header_frame.pack(side="top", fill="x", padx=10, pady=5)
        tk.Label(header_frame, text="一覧", font=("Arial", 14, "bold")).pack(side="left")
        tk.Button(header_frame, text="検索", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: master.show_frame("SearchScreen")).pack(side="right", padx=5)

        # スクロールエリア
        self.canvas = tk.Canvas(self)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.frame_result = tk.Frame(self.canvas)
        self.window_id = self.canvas.create_window((0, 0), window=self.frame_result, anchor="nw")

        self.canvas.bind("<Enter>", lambda _: self.canvas.bind_all("<MouseWheel>", self._on_mousewheel))
        self.canvas.bind("<Leave>", lambda _: self.canvas.unbind_all("<MouseWheel>"))
        self.frame_result.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_resize)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def update_data(self):
        # 既存ウィジェットを削除
        for widget in self.frame_result.winfo_children():
            widget.destroy()

        # データの取得
        rows = getattr(self.master, 'search_result', [])
        if not rows:
            tk.Label(self.frame_result, text="検索結果がありません", font=("Arial", 12), fg="gray",pady=20).pack(fill="x")
            return
        for row in rows:
            # 1行分の枠
            frame_record = tk.Frame(self.frame_result, bg=self.bgcolor, height=self.row_height, bd=1, relief="flat")
            frame_record.pack(fill="x", side="top", pady=1)
            frame_record.pack_propagate(False)
            #
            tk.Button(frame_record, text="詳細", font=("Arial", 10),
                            command=lambda r=row: self.on_button_click(r)).place(x=5, y=5, width=45, height=30)
            tk.Label(frame_record, text=f"{cnv_txt(row['type'])}", bg=self.bgcolor, 
                     font=("Arial", 10), anchor="w").place(x=70, y=0, width=120, height=self.row_height)
            tk.Label(frame_record, text=row['title'], bg=self.bgcolor, 
                     font=("Arial", 10), anchor="w").place(x=200, y=0, width=300, height=self.row_height)

    def on_button_click(self, row):
        self.master.report_id = row["id"]
        self.master.show_frame("DetailScreen")

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_resize(self, event):
        self.canvas.itemconfig(self.window_id, width=event.width)

    # def set_search(self, sql ,params):
    #     db = DBAccess().search(sql ,params)
    #     print(db)