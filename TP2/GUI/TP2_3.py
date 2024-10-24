from tkinter import *
from Utils import *
from TP2.Models.TP2_2 import average, median
from TP2.Models.TP2_3 import variance, std_dev


def variance_stddev_init(tab):
    """
    Initialize the Variance & Standard Deviation GUI contents.
    :param tab: the master ttk element
    """

    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()

    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(fill=BOTH, expand=True)

    # set the title
    ttk.Label(frame, text='Variance & Standard Deviation Calculator', font=('Courier', 17, 'bold')).grid(row=0, column=0, columnspan = 2, padx=5, pady=20)

    # create the input elements
    ttk.Label(frame, text="Prices to analyze:").grid(row=1, column=0, columnspan = 2, padx=5, pady=(20, 12))
    values = StringVar()
    format_ = StringVar()
    format_.set('Manual CSV')
    entry = ttk.Entry(frame, textvariable=values, width=25)
    entry.grid(row=2, column=0, padx=5, pady=(8, 20), sticky = E)
    ttk.OptionMenu(frame, format_, 'Manual CSV', 'JSON file', 'CSV file', 'Manual CSV').grid(row=2, column=1, padx=5, pady=(8, 20), sticky = W)

    # set the grid configuration of the frame
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    # set the result elements (without displaying them)
    label = ttk.Label(frame, font = ('Courier', 12, 'bold'))
    separator = ttk.Separator(frame, orient = HORIZONTAL)

    # set the button
    button = ttk.Button(frame, text='Calculate', command=lambda: analyze(label, separator, values.get(), format_.get()))
    button.grid(row=3, column=0, columnspan = 2, padx=5, pady=12)

    # focus on the entry element and bind it to the Enter keys
    entry.focus()
    entry.bind('<Return>', lambda event: button.invoke())
    entry.bind('<KP_Enter>', lambda event: button.invoke())


def analyze(label, separator, values, format_):
    """
    Analyzes the given values and displays the results.
    :param label: the label to display
    :param separator: the separator to display
    :param values: the values to analyze
    :param format_: the format of the values to analyze
    """

    # display the elements to show the results
    separator.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 20, sticky = EW)
    label.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

    arr: list = []

    match format_:
        case 'Manual CSV':
            arr = get_csv_capitalized(values)
        case 'JSON file':
            try:
                arr = get_list_from_json(values)
            except FileNotFoundError:
                label.config(text = 'JSON file not found')
                return
        case 'CSV file':
            try:
                arr = get_list_from_csv(values)
            except FileNotFoundError:
                label.config(text = 'CSV file not found')
                return
        case _:
            label.config(text = f'Invalid format: {format_}')
            return

    if len(arr) == 0:
        label.config(text = 'No results found.')
        return


    arr_float: List[float] = []

    # make sure the values are numbers
    for value in arr:
        try:
            arr_float.append(float(value))
        except ValueError:
            label.config(text = 'Invalid format')
            return

    # DEBUG
    print(f'values: {arr_float}')

    # calculate the variance and the standard deviation
    avg = set_precision(average(*arr_float))
    med = set_precision(median(*arr_float))
    var = set_precision(variance(*arr_float))
    stddev = set_precision(std_dev(*arr_float))

    # display the result in the GUI
    label.config(text = f"""
    The average is {avg} and the median is {med}
    The variance is {var} and its standard deviation is {stddev}""")
