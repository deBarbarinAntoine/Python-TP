from tkinter import *
from TP2.Models.TP2_4 import *


def dice_thrower_init(tab):
    """
    Initialize the Dice Thrower GUI contents.
    :param tab: the master ttk element
    """

    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()

    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)

    # set the title
    ttk.Label(frame, text = "Dice Thrower", font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)
    
    # set the number of sides for the dice
    nb_data_label = ttk.Label(frame, text = 'Number of sides')
    nb_data_label.grid(row = 1, column = 0, padx = 5, pady = (12, 5), sticky = E)
    nb_sides = IntVar(value = 6)
    spinbox_nb_sides = ttk.Spinbox(frame, from_ = 4, to = 24, increment = 1, textvariable = nb_sides, width = 2)
    spinbox_nb_sides.grid(row = 1, column = 1, padx = 5, pady = (12, 5), sticky = W)
    
    # set the number of throws
    ttk.Label(frame, text = 'Nº of throws').grid(row = 2, column = 0, padx = 5, pady = (5, 12), sticky = E)
    nb_data = IntVar(value = 100)
    spinbox_nb_data = ttk.Spinbox(frame, from_ = 0, to = 100_000, increment = 1, textvariable = nb_data, width = 6)
    spinbox_nb_data.grid(row = 2, column = 1, padx = 5, pady = (5, 12), sticky = W)

    # set the grid configuration of the frame
    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 1)

    # set the result elements (without displaying them)
    separator = ttk.Separator(frame, orient = HORIZONTAL)
    image_ctn = ttk.Frame(frame)

    # set the button
    button = ttk.Button(frame, text = 'Analyze', command = lambda: analyze(image_ctn, separator, nb_sides, nb_data))
    button.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 12)

    # focus on the entry element and bind it to the Enter keys
    spinbox_nb_data.focus()
    for widget in [spinbox_nb_data, spinbox_nb_sides]:
        widget.bind('<Return>', lambda event: button.invoke())
        widget.bind('<KP_Enter>', lambda event: button.invoke())


def analyze(image_ctn: ttk.Frame, separator: ttk.Separator, nb_sides: IntVar, nb_data: IntVar):
    """
    Analyzes the given values and displays the results.
    :param image_ctn: the image to display
    :param separator: the separator to display
    :param nb_data: the number of throws
    :param nb_sides: the number of sides
    """
    
    # check the values
    if nb_data.get() < 1:
        nb_data.set(1)
    if nb_data.get() > 100_000:
        nb_data.set(100_000)

    if nb_sides.get() < 4:
        nb_sides.set(4)
    if nb_sides.get() > 24:
        nb_sides.set(24)
    
    # generate the values
    arr: list = gen_array(len_range = (nb_data.get(), nb_data.get()), val_range = (1, nb_sides.get()))
    
    # create dictionary of {value: occurrences}
    dict_occurrences: dict = list_to_dict(arr)
    
    # close all opened graphs
    plt.close('all')
    
    # draw the bar graph
    bar_graph_draw(dict_occurrences, image_ctn)

    # display the result in the GUI
    separator.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 20, sticky = EW)
    image_ctn.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = EW)
