from datetime import date
from tkinter import *
from tkinter import ttk, messagebox
from TP1.Models import TP1_5


def leap_year_init(tab):
    """
    Initialize the Leap Year GUI content
    :param tab: the master ttk element
    """
    
    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()

    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(expand = True, fill = BOTH)

    # set the title
    ttk.Label(frame, text = 'Leap Year Checker', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)

    # create the input elements
    year = StringVar()
    year.set(str(date.today().year))
    ttk.Label(frame, text= 'Year').grid(row = 1, column = 0, padx = 5, pady = 20, sticky = E)
    spinbox = ttk.Spinbox(frame, from_ = -90_000, to = 100_000, increment = 1, textvariable = year, width = 6)
    spinbox.grid(row = 1, column = 1, padx = 5, pady = 20, sticky = W)

    # set the grid configuration of the frame
    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 1)
    
    # set the result elements (without displaying them)
    label = ttk.Label(frame, font = ('Courier', 12, 'bold'))
    separator = ttk.Separator(frame, orient = HORIZONTAL)

    # set the button
    button = ttk.Button(frame, text = 'Check', command = lambda : check(label, separator, year.get()))
    button.grid(row = 2, column = 0, columnspan = 2, pady = 12)

    # focus on the entry element and bind it to the Enter keys
    spinbox.focus()
    spinbox.bind('<Return>', lambda e: button.invoke())
    spinbox.bind('<KP_Enter>', lambda e: button.invoke())


def check(label, separator, year):
    """
    Check if the year is leap year and display the result in the GUI.
    
    Displays a messagebox if the year is invalid or not in range.
    
    :param label: the Label element to display the result
    :param separator: the Separator element
    :param year: the year to check
    """
    
    # attempt to convert year to an integer
    try:
        year = int(year)
    except ValueError:
        messagebox.showerror('Error', 'Invalid Year')
        return
    
    # check if year is in the acceptable range
    if year < -90_000 or year > 100_000:
        messagebox.showinfo('Error', 'Year must be between -90.000 and 100.000!')
        return
    
    # set the result message
    if TP1_5.is_leap_year(year):
       message: str = 'is a leap year'
    else:
        message: str = 'is not a leap year'
        
    # set and display the result in the GUI
    label.configure(text = f'The year {year} {message}')
    separator.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 20, sticky = EW)
    label.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)