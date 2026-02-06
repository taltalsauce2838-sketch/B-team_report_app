import tkinter as tk
import json
from screens.DBAccess import DBAccess
from utils import cnv_txt

# 詳細
class DetailScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        id = self.master.report_id
        # 表示対象を取得
        id = 1
        self.record = DBAccess().get(id)
        typ = cnv_txt(self.record.get("type"))
        #
        frame = tk.Frame(self)
        frame.pack(side="top", fill="x", padx=10, pady=5)
        tk.Label(frame, text=f"詳細：{typ}", font=("Arial", 14, "bold")).pack(side="left")
        tk.Button(frame, text="検索", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: master.show_frame("SearchScreen")).pack(side="right", padx=5)
        tk.Button(frame, text="検索結果", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: master.show_frame("SearchResultScreen")).pack(side="right", padx=5)
        #
        frame = tk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=5)
        text = tk.Text(frame, wrap="word", height=20)
        text.pack(side="left", fill="both", expand=True)
        scrollbar = tk.Scrollbar(frame, command=text.yview)
        scrollbar.pack(side="right", fill="y")
        text.config(yscrollcommand=scrollbar.set)
        #
        frame = tk.Frame(self)
        frame.pack(side="bottom", fill="x", padx=5, pady=10)
        tk.Label(frame, text=f"クリップボードへコピー", font=("Arial", 14, "bold")).pack(side="left")
        tk.Button(frame, text="Notion形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_to_clipboard("Notion")).pack(side="right", padx=5)
        tk.Button(frame, text="Jira形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_to_clipboard("Jira")).pack(side="right", padx=5)
        tk.Button(frame, text="Slack形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_to_clipboard("Slack")).pack(side="right", padx=5)
        # 
        if self.record is None:
            text.insert(tk.END, "該当レコードなし")
            return
        #
        # 太字タグ設定
        text.tag_configure("bold_key", font=("Arial", 10, "bold"), foreground="blue") # 太字用タグの設定
        # 出力
        for key, value in self.record.items():
            if key == "meta_json" and value:
                meta = json.loads(value)
                for m_key, m_value in meta.items():
                    text.insert(tk.END, f"{cnv_txt(m_key)}\n", "bold_key")
                    text.insert(tk.END, f"{m_value}\n\n")
            elif key in ("title", "body"):
                text.insert(tk.END, f"{cnv_txt(key)}\n", "bold_key")
                text.insert(tk.END, f"{value}\n\n")
        text.config(state=tk.DISABLED) # 編集不可

    # クリップボードへのコピー時のフォーマット
    def decorate_key(self, fmt, key):
        key = cnv_txt(key)
        if fmt == "Slack":
            return f"*{key}*"
        elif fmt == "Jira":
            return f"**{key}**"
        else:  # Notion / デフォルト
            return key

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

        # Tkinterでクリップボード操作
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text_to_copy)
        r.update() # クリップボードに反映
        r.destroy()
