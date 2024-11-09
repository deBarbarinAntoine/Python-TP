from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from ttkthemes import ThemedTk
from TP1 import *
from TP2 import *


def quit_app(window):
    """
    Quit the application by destroying the main window and exiting with code 0.
    :param window: the main window
    """
    for widget in window.winfo_children():
        widget.destroy()
        plt.close('all')

    window.destroy()
    exit(0)

def main_window():
    """
    Sets and creates the main window.
    """
    
    # setting the main window
    window = ThemedTk(theme = "arc")
    window.geometry(f'{window.winfo_screenwidth()}x{window.winfo_screenheight()}')
    window.title('TP Python - Antoine de Barbarin')
    icon = PhotoImage(file = "Data/python.png")
    window.iconphoto(True, icon)

    # make sure the background color of the frames is the one provided here
    style = ttk.Style()
    style.configure("TFrame", background= '#f5f6f7')
    
    # creating the tab controller
    tab_control = ttk.Notebook(window)
    tab_control.pack(expand = True, fill = BOTH)
    
    # creating the tab for TP1
    tab_tp1 = ttk.Frame(tab_control)
    tab_control.add(tab_tp1, text = 'TP 1', sticky = NSEW)

    # creating the content frame for TP1
    content_tp1 = ttk.Frame(tab_tp1)
    content_tp1.grid(column = 2, row = 0, ipadx = 30, ipady = 30, sticky = NSEW, padx = (0, 30))

    # creating the separator between the navigation frame and the content frame
    separator = ttk.Separator(tab_tp1, orient = VERTICAL)
    separator.grid(column = 1, row = 0, padx = 30, pady = 30, sticky = NSEW)

    # creating the navigation frame for TP1 with its buttons
    nav_tp1 = ttk.Frame(tab_tp1)
    ttk.Button(nav_tp1, text = '1. Temperature Converter', command = lambda: temp_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '2. Sum and Product of Even Numbers', command = lambda: num_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '3. Welcome Message Generator', command = lambda: greet_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '4. Mental Arithmetic Game', command = lambda: game_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '5. Leap Year Checker', command = lambda: leap_year_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = 'Quit', command = lambda : quit_app(window), padding = '10').pack(padx = 30, pady = 30, fill = X, side = BOTTOM)
    nav_tp1.grid(column = 0, row = 0, sticky = NSEW)

    # setting the grid configuration of the elements
    tab_tp1.grid_rowconfigure(0, weight=1)
    nav_tp1.grid_rowconfigure(0, weight=1)
    separator.grid_rowconfigure(0, weight=1)

    tab_tp1.grid_columnconfigure(0, weight = 1)
    tab_tp1.grid_columnconfigure(1, weight = 0)
    tab_tp1.grid_columnconfigure(2, weight = 4)

    # creating the tab for TP2
    tab_tp2 = ttk.Frame(tab_control)
    tab_control.add(tab_tp2, text = 'TP 2', sticky = NSEW)

    # creating the content frame for TP2
    content_tp2 = ttk.Frame(tab_tp2)
    content_tp2.grid(column = 2, row = 0, ipadx = 30, ipady = 30, sticky = NSEW, padx = (0, 30))

    # creating the separator between the navigation frame and the content frame
    separator = ttk.Separator(tab_tp2, orient = VERTICAL)
    separator.grid(column = 1, row = 0, padx = 30, pady = 30, sticky = NSEW)

    # creating the navigation frame for TP2 with its buttons
    nav_tp2 = ttk.Frame(tab_tp2)
    ttk.Button(nav_tp2, text = '1. Perfect Number Checker', command = lambda: perfect_num_init(content_tp2), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp2, text = '2. Average & Median Calculator', command = lambda: avg_median_init(content_tp2), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp2, text = '3. Variance & Standard Deviation Calculator', command = lambda: variance_stddev_init(content_tp2), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp2, text = '4. Age Group Analyzer', command = lambda: age_analyzer_init(content_tp2), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp2, text = '5. Dice Thrower', command = lambda: dice_thrower_init(content_tp2), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp2, text = 'Quit', command = lambda : quit_app(window), padding = '10').pack(padx = 30, pady = 30, fill = X, side = BOTTOM)
    nav_tp2.grid(column = 0, row = 0, sticky = NSEW)

    # setting the grid configuration of the elements
    tab_tp2.grid_rowconfigure(0, weight=1)
    nav_tp2.grid_rowconfigure(0, weight=1)
    separator.grid_rowconfigure(0, weight=1)

    tab_tp2.grid_columnconfigure(0, weight = 1)
    tab_tp2.grid_columnconfigure(1, weight = 0)
    tab_tp2.grid_columnconfigure(2, weight = 4)

    # creating the tab for TP3
    tab_tp3 = ttk.Frame(tab_control)
    tab_control.add(tab_tp3, text = 'TP 3', sticky = NSEW)
    
    # display the tab controller
    tab_control.pack(expand = True, fill = BOTH, side = TOP)
    
    # wait for events
    window.mainloop()

# entry point
if __name__ == '__main__': main_window()