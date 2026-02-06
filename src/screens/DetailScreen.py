import tkinter as tk
import json
from screens.DBAccess import DBAccess
from utils import cnv_txt

# 詳細
class DetailScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        # 固定ヘッダー
        frame = tk.Frame(self)
        frame.pack(side="top", fill="x", padx=10, pady=5)
        
        self.title_label = tk.Label(frame, text="詳細：", font=("Arial", 14, "bold"))
        self.title_label.pack(side="left")

        tk.Button(frame, text="検索", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: master.show_frame("SearchScreen")).pack(side="right", padx=5)
        tk.Button(frame, text="検索結果", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: master.show_frame("SearchResultScreen")).pack(side="right", padx=5)

        # テキストエリア
        frame_txt = tk.Frame(self)
        frame_txt.pack(fill="both", expand=True, padx=10, pady=5)
        self.text_widget = tk.Text(frame_txt, wrap="word", height=20)
        self.text_widget.pack(side="left", fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(frame_txt, command=self.text_widget.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_widget.config(yscrollcommand=scrollbar.set)
        self.text_widget.tag_configure("bold_key", font=("Arial", 10, "bold"), foreground="blue")

        # クリップボードへコピー
        frame_ft = tk.Frame(self)
        frame_ft.pack(side="bottom", fill="x", padx=5, pady=10)
        tk.Label(frame_ft, text="クリップボードへコピー", font=("Arial", 14, "bold")).pack(side="left")
        
        tk.Button(frame_ft, text="Notion形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_to_clipboard("Notion")).pack(side="right", padx=5)
        tk.Button(frame_ft, text="Jira形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_to_clipboard("Jira")).pack(side="right", padx=5)
        tk.Button(frame_ft, text="Slack形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_to_clipboard("Slack")).pack(side="right", padx=5)

    def update_data(self):
        id = self.master.report_id
        self.record = DBAccess().get(id)
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete("1.0", tk.END)

        typ = cnv_txt(self.record.get("type"))
        self.title_label.config(text=f"詳細：{typ}")

        for key, value in self.record.items():
            if key == "meta_json" and value:
                meta = json.loads(value)
                for m_key, m_value in meta.items():
                    self.text_widget.insert(tk.END, f"{cnv_txt(m_key)}\n", "bold_key")
                    self.text_widget.insert(tk.END, f"{m_value}\n\n")
            elif key in ("title", "body"):
                self.text_widget.insert(tk.END, f"{cnv_txt(key)}\n", "bold_key")
                self.text_widget.insert(tk.END, f"{value}\n\n")
        
        self.text_widget.config(state=tk.DISABLED)

    def decorate_key(self, fmt, key):
        key = cnv_txt(key)
        if fmt == "Slack": return f"*{key}*"
        elif fmt == "Jira": return f"**{key}**"
        else: return key

    def copy_to_clipboard(self, fmt=None):
        lines = []
        for k, v in self.record.items():
            if k == "meta_json" and v:
                meta = json.loads(v)
                for mk, mv in meta.items():
                    lines.append(self.decorate_key(fmt, mk))
                    lines.append(str(mv))
            else:
                lines.append(self.decorate_key(fmt, k))
                lines.append(str(v))
            lines.append("")
        
        text_to_copy = "\n".join(lines)
        self.clipboard_clear()
        self.clipboard_append(text_to_copy)
        self.update()