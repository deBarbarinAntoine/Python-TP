from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from TP1.GUI.TP1_1 import temp_init
from TP1.GUI.TP1_2 import num_init
from TP1.GUI.TP1_3 import greet_init
from TP1.GUI.TP1_4 import game_init
from TP1.GUI.TP1_5 import leap_year_init


def quit_app(window):
    """
    Quit the application by destroying the main window and exiting with code 0.
    :param window: the main window
    """
    window.destroy()
    exit(0)

def main_window():
    """
    Sets and creates the main window.
    :return: 
    """
    
    # setting the main window
    window = ThemedTk(theme = "arc")
    window.geometry('1024x768')
    window.title('TP Python - Antoine de Barbarin')
    
    # creating the tab controller
    tab_control = ttk.Notebook(window)
    tab_control.pack(expand = True, fill = BOTH)
    
    # creating the tab for TP1
    tab_tp1 = ttk.Frame(tab_control)
    tab_control.add(tab_tp1, text = 'TP 1', sticky = NSEW)

    # creating the navigation frame for TP1 with its buttons
    nav_tp1 = ttk.Frame(tab_tp1)
    ttk.Button(nav_tp1, text = '1. Temperature Converter', command = lambda: temp_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '2. Sum and Product of Even Numbers', command = lambda: num_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '3. Welcome Message Generator', command = lambda: greet_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '4. Mental Arithmetic Game', command = lambda: game_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = '5. Leap Year Checker', command = lambda: leap_year_init(content_tp1), padding = '10').pack(padx = 30, pady = 30, fill = X)
    ttk.Button(nav_tp1, text = 'Quit', command = lambda : quit_app(window), padding = '10').pack(padx = 30, pady = 30, fill = X, side = BOTTOM)
    nav_tp1.grid(column = 0, row = 0, sticky = NSEW)
    
    # creating the separator between the navigation frame and the content frame
    separator = ttk.Separator(tab_tp1, orient = VERTICAL)
    separator.grid(column = 1, row = 0, padx = 30, pady = 30, sticky = NSEW)
    
    # creating the content frame for TP1
    content_tp1 = ttk.Frame(tab_tp1)
    content_tp1.grid(column = 2, row = 0, ipadx = 30, ipady = 30, sticky = NSEW, padx = (0, 30))

    # creating the tab for TP2
    tab_tp2 = ttk.Frame(tab_control)
    tab_control.add(tab_tp2, text = 'TP 2', sticky = NSEW)

    # creating the tab for TP3
    tab_tp3 = ttk.Frame(tab_control)
    tab_control.add(tab_tp3, text = 'TP 3', sticky = NSEW)
    
    # display the tab controller
    tab_control.pack(expand = True, fill = BOTH, side = TOP)

    # setting the grid configuration of the elements
    tab_tp1.grid_rowconfigure(0, weight=1)
    nav_tp1.grid_rowconfigure(0, weight=1)
    separator.grid_rowconfigure(0, weight=1)
    
    tab_tp1.grid_columnconfigure(0, weight = 1)
    tab_tp1.grid_columnconfigure(1, weight = 0)
    tab_tp1.grid_columnconfigure(2, weight = 4)
    
    # wait for events
    window.mainloop()

# entry point
if __name__ == '__main__': main_window()