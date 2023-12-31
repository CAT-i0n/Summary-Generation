import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import ttk
from .ml_summary import MLSummary
from .sentence_summary import SentenceSummarizer
from .keywords_summary import KeywordsSummarizer 
import re
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-type', 'splash')
        self.title('Editor')
        self.geometry("800x800")
        self.ml_summarizer = MLSummary()
        self.sentence_summarizer = SentenceSummarizer()
        self.keyword_summarizer = KeywordsSummarizer()
        self.__build()

    def __build(self):
        # Button to quit the app.
        options_frame = tk.Frame(self)
        options_frame.pack()
        quit_button = tk.Button(options_frame, text="Quit", command=self.destroy)
        quit_button.pack(side=tk.RIGHT)

        help_button = tk.Button(options_frame, text="Help", command=self.open_help)
        help_button.pack(side=tk.LEFT)

        # Entry to type search string.
        search_frame = tk.Frame(self)
        search_frame.pack()

        # Button to run main script.
        self.method_box = ttk.Combobox(
            master = search_frame,
            state="readonly",
            values=["Key Words summary", "Sentences summary", "ML summary"]
        )
        self.method_box.pack(side=tk.LEFT)
        self.method_box.set("ML summary")
        
        go_button = tk.Button(search_frame, text="Summary", command=self.generate_summary)
        go_button.pack()

        # Text box to display output of main text.
        self.text_box = ScrolledText(
            width=100, height = 20,  borderwidth=2, relief="sunken", padx=20, font=("Helvetica", 15))
        self.text_box.pack()

        self.summary_box = ScrolledText(
            width=110, borderwidth=2, relief="sunken", padx=20, font=("Helvetica", 15))
        self.summary_box.pack()

        # Button to clear the text box display.
        clear_button = tk.Button(
            self, text="Clear", command=lambda: self.text_box.delete("1.0", tk.END))
        clear_button.pack()


    def generate_summary(self):
        file = filedialog.askopenfilename()
        text_lang = file.split('/')[-2]

        text = open(file).read()
        method = self.method_box.current()
        match method:
            case 0:
                summary = self.keyword_summarizer.generate_summary(text, text_lang)
            case 1:
                summary = self.sentence_summarizer.generate_summary(text, text_lang)
            case 2:
                summary = self.ml_summarizer.generate_summary(text, text_lang)

        self.print_to_textbox(text, summary)


    def print_to_textbox(self, text, summary):
        self.text_box.delete("1.0", tk.END)
        self.summary_box.delete("1.0", tk.END)

        self.text_box.insert("end", text)
        self.summary_box.insert("end", summary)


    def open_help(self):
        top = tk.Toplevel()
        #top.geometry("180x100")
        top.attributes('-type', 'splash')
        top.title('Editor')
        l2 = tk.Label(top, text = """
Выберете документ в файловой систему и нажмите Summary,
чтобы получить реферат
Нажмите Quit, чтобы выйти из системы
Нажмите Help, чтобы получить справку
                                """)
        l2.pack()
        quit_button = tk.Button(top, text="Quit", command=top.destroy)
        quit_button.pack(side=tk.BOTTOM)

        top.mainloop()

    def run(self):
        self.mainloop()
