from tkinter import ttk
from tkinter import *
import Utils
from TP1.Models import TP1_3


class GreetModule:
    def __init__(self):
        self.text = None
    
    @staticmethod
    def new(master):
        greet_module = GreetModule()
        greet_module.text = Text(master, width = 45, height = 7)
        return greet_module
    
    def refresh(self, greetings):
        self.text.config(state = NORMAL)
        self.text.delete('1.0', END)
        
        for greeting in greetings:
            self.text.insert(INSERT, greeting)
            self.text.insert(INSERT, '\n')
            
        height = len(greetings)
        if height > 11:
            height = 12
        elif height < 3:
            height = 3
    
        self.text.config(height = height, state = DISABLED)
        self.text.grid(row = 4, column = 0, padx = 5, pady = 25, ipadx = 5, ipady = 5)

def greet_init(tab):
    for child in tab.winfo_children():
        child.destroy()
        
    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)
    
    frame.grid_columnconfigure(0, weight = 1)
    
    ttk.Label(frame, text = 'Welcome Message Generator', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, padx = 5, pady = 20)
    
    ttk.Label(frame, text="Type a list of names (separated by comma [CSV]):").grid(row = 1, column = 0, padx = 5, pady = 8)
    names = StringVar()
    entry = ttk.Entry(frame, textvariable = names, width = 25)
    entry.grid(row = 2, column = 0, padx = 5, pady = 8)
    greet_module = GreetModule.new(frame)
    
    button = ttk.Button(frame, text = 'Validate', command = lambda : compose(greet_module, names.get()))
    button.grid(row = 3, column = 0, padx = 5, pady = 12)
    entry.focus()
    entry.bind('<Return>', lambda event: button.invoke())
    entry.bind('<KP_Enter>', lambda event: button.invoke())

def compose(greet_module, names):
    names = Utils.get_csv_capitalized(names)
    greetings = TP1_3.assign_random_greeting(names)
    greet_module.refresh(greetings)
