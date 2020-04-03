#!/usr/bin/python

import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class App(ttk.Frame):
    def __init__(self, master):
        self.master = master
        super().__init__(master)

        top = ttk.Frame()
        bot = ttk.Frame()

        top.pack(ipadx=3, ipady=3)
        bot.pack(ipadx=3, ipady=3)

        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, 0.01)
        fig.add_subplot(111).plot(t, np.sin(2 * np.pi * t))

        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=5, pady=5)

        lbl_f = ttk.Label(bot, text='F: ')
        lbl_fs = ttk.Label(bot, text='Fs: ')
        lbl_order = ttk.Label(bot, text='N: ')

        ent_f = ttk.Entry(bot)
        ent_fs = ttk.Entry(bot)
        ent_order = ttk.Entry(bot)

        but = ttk.Button(bot, text='Hi')

        lbl_f.pack(side='left')
        ent_f.pack(side='left')

        lbl_fs.pack(side='left')
        ent_fs.pack(side='left')

        lbl_order.pack(side='left')
        ent_order.pack(side='left')

        but.pack(side='left')


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()

