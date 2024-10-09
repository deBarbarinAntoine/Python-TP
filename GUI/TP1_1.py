from tkinter import ttk, StringVar, messagebox, Text, IntVar
from tkinter.constants import INSERT, DISABLED
import Utils
from TP1 import TP1_1

def temp_init(tab):
    for child in tab.winfo_children():
        child.destroy()
    ttk.Label(tab, text="Choose a unit:").grid(column=2, row=0, columnspan=2)
    unit = IntVar()
    ttk.Radiobutton(tab, text='Fahrenheit', variable=unit, value=0).grid(column=2, row=1)
    ttk.Radiobutton(tab, text='Celsius', variable=unit, value=1).grid(column=3, row=1)
    ttk.Label(tab, text="Type a Temperature:").grid(column=2, row=2, columnspan=2)
    temp = StringVar()
    ttk.Entry(tab, textvariable=temp).grid(column=2, row=3)
    ttk.Button(tab, text='Convert', command=lambda : convert(tab, temp.get(), unit.get())).grid(column=2, row=4, columnspan=2)

def convert(tab, temp, unit):
    match unit:
        case 0:
            unit = TP1_1.Temperature.Unit.Fahrenheit
        case 1:
            unit = TP1_1.Temperature.Unit.Celsius
        case _:
            messagebox.showerror('Error', 'Unexpected unit')
            return
    try:
        temperature = TP1_1.Temperature.new(float(temp))
    except ValueError:
        messagebox.showerror('Error', 'Invalid Temperature')
        return
    ttk.Separator(tab, orient='horizontal').grid(column=2, row=5)
    try:
        converted_temp, converted_unit = temperature.convert(unit)
        converted_temp = Utils.set_precision(converted_temp)
    except ValueError as e:
        messagebox.showerror('Error', str(e))
        return
    text = Text(tab)
    text.insert(INSERT, f'{temp}{unit.str()} is equivalent to {converted_temp}{converted_unit.str()}')
    text.config(state=DISABLED)
    text.grid(column=2, row=6, columnspan=2)
