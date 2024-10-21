from tkinter import *
from tkinter import ttk

from ttkthemes import ThemedTk
from TP1.GUI.TP1_1 import temp_init
from TP1.GUI.TP1_2 import num_init
from TP1.GUI.TP1_3 import greet_init
from TP1.GUI.TP1_4 import game_init
from TP1.GUI.TP1_5 import leap_year_init


def quit_app(window):
    window.destroy()
    exit(0)

def main_window():
    
    window = ThemedTk(theme = "arc")
    window.geometry('800x450')
    window.title('TP Python - Antoine de Barbarin')
    
    tab_control = ttk.Notebook(window)
    tab_control.pack(expand = True, fill = BOTH)
    
    tab_tp1 = ttk.Frame(tab_control)
    tab_control.add(tab_tp1, text = 'TP 1', sticky = 'nsew')

    nav_tp1 = ttk.Frame(tab_tp1)
    content_tp1 = ttk.Frame(tab_tp1)
    ttk.Button(nav_tp1, text = 'Temperature Converter', command = lambda: temp_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = 'Sum and Product of Even Numbers', command = lambda: num_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = 'Welcome Message Generator', command = lambda: greet_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = 'Mental Arithmetic Game', command = lambda: game_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = 'Leap Year Checker', command = lambda: leap_year_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    
    ttk.Button(nav_tp1, text = 'Quit', command = lambda : quit_app(window), padding = '10').pack(padx = 30, pady = 30, fill = X, side = BOTTOM)
    
    nav_tp1.grid(column = 0, row = 0, sticky = 'nsew')
    separator = ttk.Separator(tab_tp1, orient = 'vertical')
    separator.grid(column = 1, row = 0, padx = 30, pady = 30, sticky = 'nsew')
    content_tp1.grid(column = 2, row = 0, ipadx = 30, ipady = 30, sticky = 'nsew', padx = (0, 30))

    tab_tp2 = ttk.Frame(tab_control)
    tab_control.add(tab_tp2, text = 'TP 2', sticky = 'nsew')

    tab_tp3 = ttk.Frame(tab_control)
    tab_control.add(tab_tp3, text = 'TP 3', sticky = 'nsew')
    tab_control.pack(expand = True, fill = BOTH, side = TOP)

    tab_tp1.grid_rowconfigure(0, weight=1)
    nav_tp1.grid_rowconfigure(0, weight=1)
    separator.grid_rowconfigure(0, weight=1)
    
    tab_tp1.grid_columnconfigure(0, weight = 1)
    tab_tp1.grid_columnconfigure(1, weight = 0)
    tab_tp1.grid_columnconfigure(2, weight = 4)
    
    window.mainloop()

if __name__ == '__main__': main_window()