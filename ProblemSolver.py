import tkinter as tk
from tkinter import ttk
import time

Large_font = ('Verdana', 12)


class Solver(tk.Tk):

    def __init__(self):

        tk.Tk.__init__(self)
        container = tk.Frame()

        container.pack(side='top', fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]

        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text='Start Page', font=Large_font)
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text='Solve Problems', command=lambda: popup())
        button.pack()


def popup():

    popup = tk.Tk()

    frame1 = tk.Frame(popup)
    frame1.pack(fill='both', padx=10)

    frame2 = tk.Frame(popup)
    frame2.pack(side='bottom')

    popup.title('Solving Problems')

    label = tk.Label(frame1, text='Solving Problems')
    label.pack(side='top', pady=10, padx=10)

    progress_bar = ttk.Progressbar(frame1, value=0, maximum=30)
    progress_bar.pack(fill='both')

    btn1 = tk.Button(frame2, text='I still have problems :(', command=lambda: popup.destroy(), state='disabled')
    btn1.pack(side='left', pady=10, padx=10)

    btn2 = tk.Button(frame2, text='Yay!', command=lambda: app.quit(), state='disabled')
    btn2.pack(side='left', pady=10, padx=10)

    popup.after(1000, lambda: func(progress_bar))


def func(pb):

    pb['value'] += 10


app = Solver()
app.geometry('275x80')
app.title('Problem Solver 1.0')
app.resizable(False, False)
app.mainloop()



