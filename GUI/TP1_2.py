from tkinter import ttk, StringVar, messagebox, Text
from tkinter.constants import INSERT, DISABLED
from TP1 import TP1_2


def num_init(tab):
    for child in tab.winfo_children():
        child.destroy()
    ttk.Label(tab, text="Type a positive integer:").grid(column=2, row=0, columnspan=2)
    num = StringVar()
    ttk.Entry(tab, textvariable=num).grid(column=2, row=1)
    ttk.Button(tab, text='Validate', command=lambda : compute(tab, num.get())).grid(column=2, row=2, columnspan=2)

def compute(tab, num):
    try:
        num = int(num)
    except ValueError:
        messagebox.showerror('Error', 'Invalid Integer')
        return
    ttk.Separator(tab, orient='horizontal').grid(column=2, row=2)
    try:
        even_numbers = TP1_2.get_even_numbers(num)
    except ValueError as e:
        messagebox.showerror('Error', str(e))
        return
    text = Text(tab)
    text.insert(INSERT, f"""
    1)   {TP1_2.get_expression(even_numbers, '+')} = {TP1_2.sum_list(even_numbers)}
    2)   {TP1_2.sum_list(even_numbers)} = {TP1_2.get_expression(even_numbers, '+')}
    3)   {TP1_2.get_expression(even_numbers, 'x')} = {TP1_2.product_list(even_numbers)}
    4)   {TP1_2.product_list(even_numbers)} = {TP1_2.get_expression(even_numbers, 'x')}""")
    text.config(state=DISABLED)
    text.grid(column=2, row=3, columnspan=2)
