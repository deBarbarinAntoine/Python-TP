from tkinter import ttk, StringVar, Text
from tkinter.constants import INSERT, DISABLED
import Utils
from TP1 import TP1_3

def greet_init(tab):
    for child in tab.winfo_children():
        child.destroy()
    ttk.Label(tab, text="Type a list of names (separated by comma [CSV]):").grid(column=2, row=0, columnspan=2)
    names = StringVar()
    ttk.Entry(tab, textvariable=names).grid(column=2, row=1)
    ttk.Button(tab, text='Validate', command=lambda : compose(tab, names.get())).grid(column=2, row=2, columnspan=2)

def compose(tab, names):
    names = Utils.get_csv_capitalized(names)
    ttk.Separator(tab, orient='horizontal').grid(column=2, row=2)
    greetings = TP1_3.assign_random_greeting(names)

    text = Text(tab)
    for greeting in greetings:
        text.insert(INSERT, greeting)
        text.insert(INSERT, '\n')
    text.config(state=DISABLED)
    text.grid(column=2, row=3, columnspan=2)
