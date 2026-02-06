
import tkinter as tk
from screens.SearchScreen import SearchScreen
from screens.SearchResultScreen import SearchResultScreen
from screens.NewRegistrationStandup import NewRegistrationStandup
from screens.NewRegistrationHandover import NewRegistrationHandover
from screens.NewRegistrationIncident import NewRegistrationIncident
from screens.DetailScreen import DetailScreen

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #
        self.search_result = ""
        self.report_id = None
        #
        self.title("title")
        self.geometry("600x400")

        self.screen_classes = {
            "SearchScreen": SearchScreen,
            "SearchResultScreen": SearchResultScreen,
            "NewRegistrationStandup": NewRegistrationStandup,
            "NewRegistrationHandover": NewRegistrationHandover,
            "NewRegistrationIncident": NewRegistrationIncident,
            "DetailScreen": DetailScreen
        }

        self.frames = {}
        for name, cls in self.screen_classes.items():
            frame = cls(self)
            self.frames[name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("SearchScreen")

    # show_frame は文字列で画面指定
    def show_frame(self, screen_name):
        frame = self.frames[screen_name]
        frame.tkraise()