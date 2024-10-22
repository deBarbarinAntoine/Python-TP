from tkinter import ttk, messagebox
from tkinter import *
from TP1.Models import TP1_2


class NumModule:
    """
    A simple module to handle the results in the GUI.
    """
    def __init__(self):
        """
        Simple constructor.
        """
        self.separator = None
        self.label1 = None
        self.label2 = None
        self.label3 = None
        self.label4 = None
    
    @staticmethod
    def new(master):
        """
        Static constructor with a ttk element as the master.
        :param master: the master ttk element
        :return: the new NumModule instance
        """
        num_module = NumModule()
        
        # setting the results GUI elements
        num_module.separator = ttk.Separator(master, orient = HORIZONTAL)
        num_module.label1 = ttk.Label(master)
        num_module.label2 = ttk.Label(master)
        num_module.label3 = ttk.Label(master)
        num_module.label4 = ttk.Label(master)
        
        return num_module
    
    def refresh(self, *results):
        """
        Refreshes the results GUI elements.
        :param results: the results
        """
        
        # setting and displaying the results
        self.separator.grid(row = 3, column = 0, columnspan = 2, pady = 20, padx = 5, sticky = EW)
        self.label1.configure(text = f'1)   {results[0]}')
        self.label2.configure(text = f'2)   {results[1]}')
        self.label3.configure(text = f'3)   {results[2]}')
        self.label4.configure(text = f'4)   {results[3]}')
        self.label1.grid(row = 4, column = 0, columnspan = 2, sticky = EW)
        self.label2.grid(row = 5, column = 0, columnspan = 2, sticky = EW)
        self.label3.grid(row = 6, column = 0, columnspan = 2, sticky = EW)
        self.label4.grid(row = 7, column = 0, columnspan = 2, sticky = EW)
        

def num_init(tab):
    """
    Initialise the Num GUI content.
    :param tab: the master ttk element
    """
    
    # destroy all children of the tab
    for child in tab.winfo_children():
        child.destroy()
    
    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)
    
    # set the title
    ttk.Label(frame, text = 'Sum & Product of Even Numbers', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)

    # create the input elements
    num = StringVar()
    num.set('6')
    ttk.Label(frame, text= 'Positive integer').grid(row = 1, column = 0, padx = 5, pady = 20, sticky = E)
    spinbox = ttk.Spinbox(frame, from_ = 0, to = 25, increment = 1, textvariable = num, width = 2)
    spinbox.grid(row = 1, column = 1, padx = 5, pady = 20, sticky = W)
    
    # set the grid configuration of the frame
    frame.grid_columnconfigure(index = 0, weight = 1)
    frame.grid_columnconfigure(index = 1, weight = 1)
    
    
    # set the button
    num_module = NumModule.new(frame)
    button = ttk.Button(frame, text='Validate', command=lambda : compute(num_module, num.get()))
    
    # focus on the entry element and bind it to the Enter keys
    spinbox.focus()
    spinbox.bind('<Return>', lambda e: button.invoke())
    spinbox.bind('<KP_Enter>', lambda e: button.invoke())
    button.grid(column=0, row=2, columnspan=2, pady = 12)

def compute(num_module, num):
    """
    Calculates the sum and product of even numbers and refreshes the NumModule (GUI).
    :param num_module: the NumModule instance
    :param num: the number
    :raise ValueError: show an error window if num is not an integer or if the operation fails
    """
    
    # attempt to convert num to an integer
    try:
        num = int(num)
    except ValueError:
        messagebox.showerror('Error', 'Invalid Integer')
        return
    
    # attempt to get the sum and product of the even numbers from 0 to num
    try:
        even_numbers = TP1_2.get_even_numbers(num)
    except ValueError as e:
        messagebox.showerror('Error', str(e))
        return
    
    # refresh the NumModule (GUI)
    num_module.refresh(
        f'{TP1_2.get_expression(even_numbers, '+')} = {TP1_2.sum_list(even_numbers)}',
        f'{TP1_2.sum_list(even_numbers)} = {TP1_2.get_expression(even_numbers, '+')}',
        f'{TP1_2.get_expression(even_numbers, 'x')} = {TP1_2.product_list(even_numbers)}',
        f'{TP1_2.product_list(even_numbers)} = {TP1_2.get_expression(even_numbers, 'x')}'
    )
