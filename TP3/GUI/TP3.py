from tkinter import *
from tkinter import ttk

from TP3.Models import *


class TP3_Module:
    """
    A simple module to handle the GUI elements of the result.
    """
    def __init__(self):
        """
        A simple constructor.
        """
        self.text: Text = None

    @staticmethod
    def new(master: ttk.Frame):
        """
        Static constructor with a ttk element as the master.
        :param master: the master ttk element
        :return: the new TP3_Module instance
        """
        tp3_module = TP3_Module()

        # setting the Text result element
        tp3_module.text = Text(master, width = 45, height = 12)
        tp3_module.text.config(state = DISABLED)

        return tp3_module

    def update(self, content: str) -> None:
        """
        Updates the text of the TP3_Module with the given content.
        :param content: the content to update the text
        :return: None
        """

        # setting the Text state to `NORMAL` to edit it
        self.text.config(state = NORMAL)

        # delete all content in the Text element
        self.text.delete('1.0', END)

        # insert the new content in the Text element
        self.text.insert(INSERT, content)
        self.text.insert(INSERT, '\n')

        # setting the Text state back to `DISABLED`
        self.text.config(state = DISABLED)

        # display the Text element in the frame
        self.text.grid(row = 1, column = 0, sticky = NSEW)


def init(tab: ttk.Frame):

    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()

    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(fill=BOTH, expand=True)

    # set the title
    ttk.Label(frame, text='TP 3 - Tests', font=('Courier', 17, 'bold')).grid(row=0, column=0, padx=5, pady=20)

    # creating a new TP3 Module in the frame
    tp3 = TP3_Module.new(frame)

    # setting the grid configuration of the elements
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_rowconfigure(2, weight=1)
    frame.grid_rowconfigure(3, weight=1)
    frame.grid_rowconfigure(4, weight=1)
    frame.grid_rowconfigure(5, weight=1)

    frame.grid_columnconfigure(0, weight = 1)

    # create the buttons to run the tests
    ttk.Button(frame, text = 'Test Book', command = lambda : tp3.update(test_book_run())).grid(row=2, column=0, padx=5)
    ttk.Button(frame, text = 'Test Library', command = lambda : tp3.update(test_library_run())).grid(row=3, column=0, padx=5)
    ttk.Button(frame, text = 'Test Boat', command = lambda : tp3.update(test_boat_run())).grid(row=4, column=0, padx=5)
    ttk.Button(frame, text = 'Test Port', command = lambda : tp3.update(test_port_run())).grid(row=5, column=0, padx=5)
    ttk.Button(frame, text = 'Test All', command = lambda : tp3.update(test_all_run())).grid(row=6, column=0, padx=5)




