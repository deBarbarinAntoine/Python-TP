from datetime import date
from tkinter import *
from tkinter import ttk, messagebox
from TP1.Models import TP1_5


def leap_year_init(tab):
    for child in tab.winfo_children():
        child.destroy()

    frame = ttk.Frame(tab)
    frame.pack(expand = True, fill = BOTH)

    ttk.Label(frame, text = 'Leap Year Checker', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)

    year = StringVar()
    year.set(str(date.today().year))
    ttk.Label(frame, text= 'Year').grid(row = 1, column = 0, padx = 5, pady = 5, sticky = E)
    spinbox = ttk.Spinbox(frame, from_ = -90_000, to = 100_000, increment = 1, textvariable = year, width = 6)
    spinbox.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 1)
    
    label = ttk.Label(frame, font = ('Courier', 12, 'bold'))
    separator = ttk.Separator(frame, orient = HORIZONTAL)

    button = ttk.Button(frame, text = 'Check', command = lambda : check(label, separator, year.get()))
    button.grid(row = 2, column = 0, columnspan = 2)

    spinbox.focus()
    spinbox.bind('<Return>', lambda e: button.invoke())
    spinbox.bind('<KP_Enter>', lambda e: button.invoke())


def check(label, separator, year):
    try:
        year = int(year)
    except ValueError:
        messagebox.showerror('Error', 'Invalid Year')
        return
    if year < -90_000 or year > 100_000:
        messagebox.showinfo('Error', 'Year must be between -90.000 and 100.000!')
        return
    if TP1_5.is_leap_year(year):
       message: str = 'is a leap year'
    else:
        message: str = 'is not a leap year'
    label.configure(text = f'The year {year} {message}')
    separator.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 20, sticky = EW)
    label.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)