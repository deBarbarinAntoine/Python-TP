from tkinter import ttk
from tkinter import *
import Utils
from TP1.Models import TP1_3


class GreetModule:
    """
    A simple module to handle the GUI elements of the result.
    """
    def __init__(self):
        """
        A simple constructor.
        """
        self.text = None
    
    @staticmethod
    def new(master):
        """
        Static constructor with a ttk element as the master.
        :param master: the master ttk element
        :return: the new GreetModule instance
        """
        greet_module = GreetModule()
        
        # setting the Text result element
        greet_module.text = Text(master, width = 45, height = 7)
        
        return greet_module
    
    def refresh(self, greetings):
        """
        Refresh the result in the GUI.
        :param greetings: the greetings
        """
        
        # setting the Text state to `NORMAL` to edit it
        self.text.config(state = NORMAL)
        
        # delete all content in the Text element
        self.text.delete('1.0', END)
        
        # insert each greeting with a newline after it
        for greeting in greetings:
            self.text.insert(INSERT, greeting)
            self.text.insert(INSERT, '\n')
            
        # setting the Text height according to the number of greetings displayed
        height = len(greetings)
        if height > 11:
            height = 12
        elif height < 3:
            height = 3
    
        # setting the Text state back to `DISABLED` and display it on the GUI
        self.text.config(height = height, state = DISABLED)
        self.text.grid(row = 4, column = 0, padx = 5, pady = 25, ipadx = 5, ipady = 5)

def greet_init(tab):
    """
    Initialize the Greetings GUI contents.
    :param tab: the master ttk element
    """
    
    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()
        
    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)
    
    # set the title
    ttk.Label(frame, text = 'Welcome Message Generator', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, padx = 5, pady = 20)
    
    # create the input elements
    ttk.Label(frame, text="Type a list of names (separated by comma [CSV]):").grid(row = 1, column = 0, padx = 5, pady = (20, 12))
    names = StringVar()
    entry = ttk.Entry(frame, textvariable = names, width = 25)
    entry.grid(row = 2, column = 0, padx = 5, pady = (8, 20))

    # set the grid configuration of the frame
    frame.grid_columnconfigure(0, weight = 1)

    # set the button
    greet_module = GreetModule.new(frame)
    button = ttk.Button(frame, text = 'Validate', command = lambda : compose(greet_module, names.get()))
    button.grid(row = 3, column = 0, padx = 5, pady = 12)
    
    # focus on the entry element and bind it to the Enter keys
    entry.focus()
    entry.bind('<Return>', lambda event: button.invoke())
    entry.bind('<KP_Enter>', lambda event: button.invoke())

def compose(greet_module, names):
    """
    Associates a random greeting to each name and refreshes the GreetModule (GUI).
    :param greet_module: the GreetModule instance
    :param names: the list of names (separated by comma [CSV])
    """
    
    # set the list of names
    names = Utils.get_csv_capitalized(names)
    
    # get the greetings with the names embedded
    greetings = TP1_3.assign_random_greeting(names)
    
    # refresh the GreetModule (GUI)
    greet_module.refresh(greetings)
