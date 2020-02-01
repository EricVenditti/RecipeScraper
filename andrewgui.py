import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from full_search import *

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


class window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self)
        tk.Tk.wm_title(self, "RecipeScraper.V1.0")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=110, column=110, sticky="nsew")  # either pack or grid

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def searchRecipe():
            looking_for = message1.get()
            print(looking_for)
            get_stuff(looking_for)

        label = ttk.Label(self, text="What food would you like to make?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        message1 = ttk.Entry(self)
        message1.pack()

        '''
        button1 = ttk.Button(self, text="Search",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
        '''
        button1 = ttk.Button(self, text="Search",
                             command=lambda: [searchRecipe(),
                                              controller.show_frame(PageOne)])
        button1.pack()

        # answer = simpledialog.askstring("Input", "Insert food item",
        #                                parent=self)
        # print(answer)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Food options displayed here", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button2 = ttk.Button(self, text="Back to Search",
                             command=lambda: controller.show_frame(StartPage))
        button2.pack()

        button3 = ttk.Button(self, text="To page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button3.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Extra Page two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button3 = ttk.Button(self, text="Back to food options",
                             command=lambda: controller.show_frame(PageOne))
        button3.pack()


app = window()
app.mainloop()
