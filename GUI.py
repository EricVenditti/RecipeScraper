import tkinter as tk

class recipeCuisine(tk.Tk):



    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        recipeCuisine1 = tk.Tk()
        w = recipeCuisine1.winfo_screenwidth()
        h = recipeCuisine1.winfo_screenheight()
        recipeCuisine1.destroy()

        container = tk.Frame(self, width=w, height=h)
        container.grid_propagate(False)
        container.pack()



        self.frames = {}
        for F in (searchPage, resultPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("searchPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()



class searchPage(tk.Frame):

    def __init__(self, parent, controller, width = 1000, height = 500):
        tk.Frame.__init__(self, parent, width = 1000, height = 500)

        label = tk.Label(self, text="What Cuisine would you like?")
        label.pack()

        button1 = tk.Button(self, text="Search",
                            command=lambda: controller.show_frame("resultPage"))

        button1.pack()


class resultPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Search for Cuisine")
        label.pack()
        button = tk.Button(self, text="Go back",
                           command=lambda: controller.show_frame("searchPage"))
        button.pack()


'''
    recipeCuisine = tk.Tk()
    width = recipeCuisine.winfo_screenwidth()
    height = recipeCuisine.winfo_screenheight()
    recipeCuisine.geometry("%dx%d" % (width, height))
'''




app = recipeCuisine()
app.mainloop()