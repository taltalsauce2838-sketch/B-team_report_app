import tkinter as tk

# 未実装のため仮の処理
def get(id):
    return """(
    'standup', 
    '', 
    '昨日：設計完了、今日：コーディング開始', 
    '{""date"": ""2026-02-04"", ""done"": ""Database schema design"", ""today"": ""Implementation of API"", ""blocker"": ""None"", ""ticket"": ""PROJ-101""}', 
    NOW(), NOW()
),
"""

# 詳細
class DetailScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        id = self.master.report_id
        # 表示対象を取得
        txt = get(id)
        typ = "日報"
        #
        frame = tk.Frame(self)
        frame.pack(side="top", fill="x", padx=10, pady=5)
        #
        tk.Label(frame, text=f"詳細：{typ}", font=("Arial", 14, "bold")).pack(side="left")
        tk.Button(frame, text="検索", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: master.show_frame("SearchScreen")).pack(side="right", padx=5)
        tk.Button(frame, text="検索結果", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: master.show_frame("SearchResultScreen")).pack(side="right", padx=5)
        #
        text = tk.Text(self, wrap="word", height=20)
        text.pack(fill="both", padx=10, pady=5, expand=True)
        text.insert("1.0", txt)
        #
        frame = tk.Frame(self)
        frame.pack(side="bottom", fill="x", padx=5, pady=10)
        tk.Label(frame, text=f"クリップボードへコピー", font=("Arial", 14, "bold")).pack(side="left")
        tk.Button(frame, text="Slack形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_slack(txt)).pack(side="right", padx=5)
        tk.Button(frame, text="Jira形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_jira(txt)).pack(side="right", padx=5)
        tk.Button(frame, text="Notion形式", font=("Arial", 12), padx=8, pady=4,
                  command=lambda: self.copy_notion(txt)).pack(side="right", padx=5)

    def copy_slack(self, txt):
        print(txt, "slack")
        pass

    def copy_jira(self, txt):
        print(txt, "jira")
        pass

    def copy_notion(self, txt):
        print(txt, "notion")
        pass
