from tkinter import *
from tkinter import ttk, messagebox
from TP2.Models import TP2_1


def perfect_num_init(tab):
    """
    Initialize the Perfect Number GUI content
    :param tab: the master ttk element
    """
    
    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()

    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(expand = True, fill = BOTH)

    # set the title
    ttk.Label(frame, text = 'Perfect Number Checker', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)

    # create the input elements
    num = StringVar()
    num.set('6')
    ttk.Label(frame, text= 'Number').grid(row = 1, column = 0, padx = 5, pady = 20, sticky = E)
    spinbox = ttk.Spinbox(frame, from_ = 0, to = 100_000_000_000, increment = 1, textvariable = num, width = 12)
    spinbox.grid(row = 1, column = 1, padx = 5, pady = 20, sticky = W)

    # set the grid configuration of the frame
    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 1)
    
    # set the result elements (without displaying them)
    label = ttk.Label(frame, font = ('Courier', 12, 'bold'))
    separator = ttk.Separator(frame, orient = HORIZONTAL)

    # set the button
    button = ttk.Button(frame, text = 'Check', command = lambda : check(label, separator, num.get()))
    button.grid(row = 2, column = 0, columnspan = 2, pady = 12)

    # focus on the entry element and bind it to the Enter keys
    spinbox.focus()
    spinbox.bind('<Return>', lambda e: button.invoke())
    spinbox.bind('<KP_Enter>', lambda e: button.invoke())


def check(label, separator, num):
    """
    Check if the number is a perfect number and display the result in the GUI.
    
    Displays a messagebox if the number is invalid or not in range.
    
    :param label: the Label element to display the result
    :param separator: the Separator element
    :param num: the number to check
    """
    
    # attempt to convert num to an integer
    try:
        num = int(num)
    except ValueError:
        messagebox.showerror('Error', 'Invalid Year')
        return
    
    # check if num is in the acceptable range
    if num < 0 or num > 100_000_000_000:
        messagebox.showinfo('Error', 'Year must be between 0 and 100.000.000.000!')
        return
    
    # set the result message
    if TP2_1.is_perfect(num):
       message: str = 'is a perfect number'
    else:
        message: str = 'is not a perfect number'
        
    # set and display the result in the GUI
    label.configure(text = f'{num} {message}')
    separator.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 20, sticky = EW)
    label.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)