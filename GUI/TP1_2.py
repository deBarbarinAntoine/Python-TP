from tkinter import ttk, messagebox
from tkinter import *

from TP1 import TP1_2

class NumModule:
    def __init__(self):
        self.separator = None
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
    
    @staticmethod
    def new(master):
        num_module = NumModule()
        num_module.separator = ttk.Separator(master, orient = HORIZONTAL)
        num_module.label1 = ttk.Label(master)
        num_module.label2 = ttk.Label(master)
        num_module.label3 = ttk.Label(master)
        num_module.label4 = ttk.Label(master)
        return num_module
    
    def refresh(self, *results):
        self.separator.grid(row = 3, column = 0, columnspan = 2, pady = 20, padx = 5, sticky = 'ew')
        self.label1.configure(text = f'1)   {results[0]}')
        self.label2.configure(text = f'2)   {results[1]}')
        self.label3.configure(text = f'3)   {results[2]}')
        self.label4.configure(text = f'4)   {results[3]}')
        self.label1.grid(row = 4, column = 0, columnspan = 2, sticky = 'ew')
        self.label2.grid(row = 5, column = 0, columnspan = 2, sticky = 'ew')
        self.label3.grid(row = 6, column = 0, columnspan = 2, sticky = 'ew')
        self.label4.grid(row = 7, column = 0, columnspan = 2, sticky = 'ew')
        

def num_init(tab):
    for child in tab.winfo_children():
        child.destroy()
    
    ttk.Label(tab, text = 'Sum & Product of Even Numbers', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)

    num = StringVar()
    num.set('6')
    ttk.Label(tab, text= 'Positive integer').grid(row = 1, column = 0, padx = 5, pady = 5)
    spinbox = ttk.Spinbox(tab, from_ = 0, to = 25, increment = 1, textvariable = num, width = 2)
    spinbox.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)
    
    num_module = NumModule.new(tab)
    
    button = ttk.Button(tab, text='Validate', command=lambda : compute(num_module, num.get()))
    
    spinbox.focus()
    spinbox.bind('<Return>', lambda e: button.invoke())
    spinbox.bind('<KP_Enter>', lambda e: button.invoke())
    button.grid(column=0, row=2, columnspan=2)

def compute(num_module, num):
    try:
        num = int(num)
    except ValueError:
        messagebox.showerror('Error', 'Invalid Integer')
        return
    try:
        even_numbers = TP1_2.get_even_numbers(num)
    except ValueError as e:
        messagebox.showerror('Error', str(e))
        return
    
    num_module.refresh(
        f'{TP1_2.get_expression(even_numbers, '+')} = {TP1_2.sum_list(even_numbers)}',
        f'{TP1_2.sum_list(even_numbers)} = {TP1_2.get_expression(even_numbers, '+')}',
        f'{TP1_2.get_expression(even_numbers, 'x')} = {TP1_2.product_list(even_numbers)}',
        f'{TP1_2.product_list(even_numbers)} = {TP1_2.get_expression(even_numbers, 'x')}'
    )
