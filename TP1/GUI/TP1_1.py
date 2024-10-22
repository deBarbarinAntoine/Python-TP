from tkinter import *
from tkinter import ttk, messagebox
import Utils
from TP1.Models import TP1_1


class TemperatureModule:
    """
    A simple module to handle the GUI elements of the result.
    """
    def __init__(self):
        """
        Simple constructor.
        """
        self.separator = None
        self.result_label = None
        
    @staticmethod
    def new(master):
        """
        Static constructor with a ttk element as the master.
        :param master: the master ttk element
        :return: the new TemperatureModule instance
        """
        temp_module = TemperatureModule()
        
        # setting the separator and label
        temp_module.separator = ttk.Separator(master, orient = HORIZONTAL)
        temp_module.result_label = ttk.Label(master, font = ('Courier', 12, 'bold'))
        
        return temp_module
    
    def refresh(self, result):
        """
        Refresh the temperature result in the GUI.
        :param result: the temperature result
        """
        self.separator.grid(column = 0, row = 3, columnspan = 3, pady = 20, padx = 5, sticky = 'ew')
        self.result_label.configure(text = result)
        self.result_label.grid(column = 0, row = 4, columnspan = 3)

def temp_init(tab):
    """
    Initialize the temperature GUI content.
    :param tab: the master ttk element
    """
    
    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()
        
    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(expand = True, fill = BOTH)
    
    # set the title
    ttk.Label(frame, text = 'Temperature Converter', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 20)

    # create the input elements
    temp = StringVar()
    unit = StringVar()
    temp.set('0')
    ttk.Label(frame, text= 'Temperature').grid(row = 1, column = 0, padx = 5, pady = 20, sticky = 'e')
    spinbox = ttk.Spinbox(frame, from_ = -459.67, to = 100_000, increment = 1, textvariable = temp, width = 6)
    spinbox.grid(row = 1, column = 1, padx = 5, pady = 20)
    ttk.OptionMenu(frame, unit, 'ºC', 'ºF', 'ºC').grid(row = 1, column = 2, padx = 5, pady = 20, sticky = 'w')
    
    # set the grid configuration of the frame
    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 0)
    frame.grid_columnconfigure(2, weight = 1)
    
    # set the button
    temp_module = TemperatureModule.new(frame)
    button = ttk.Button(frame, text = 'Convert', command = lambda : convert(temp_module, temp.get(), unit.get()))
    button.grid(column = 0, row = 2, columnspan = 3, pady = 12)
    
    # focus on the entry element and bind it to the Enter keys
    spinbox.focus()
    spinbox.bind('<Return>', lambda e: button.invoke())
    spinbox.bind('<KP_Enter>', lambda e: button.invoke())
    

def convert(temp_module, temp, unit):
    """
    Converts the temperature and refreshes the temperature module (GUI).
    :param temp_module: the temperature module
    :param temp: the temperature to convert
    :param unit: the unit to convert from
    :raise ValueError: if either the temperature or unit is invalid 
    """
    
    # check the unit
    match unit:
        case 'ºF':
            unit = TP1_1.Temperature.Unit.Fahrenheit
        case 'ºC':
            unit = TP1_1.Temperature.Unit.Celsius
            
        # invalid unit
        case _:
            messagebox.showerror('Error', 'Unexpected unit')
            return
    # attempt to create a new temperature
    try:
        temperature = TP1_1.Temperature.new(float(temp))
    except ValueError:
        messagebox.showerror('Error', 'Invalid Temperature')
        return
    
    # attempt to convert the temperature
    try:
        converted_temp, converted_unit = temperature.convert(unit)
        converted_temp = Utils.set_precision(converted_temp)
    except ValueError as e:
        messagebox.showerror('Error', str(e))
        return
    
    # refresh the temperature module (GUI)
    temp_module.refresh(f'{temp}{unit.str()} = {converted_temp}{converted_unit.str()}')
    
