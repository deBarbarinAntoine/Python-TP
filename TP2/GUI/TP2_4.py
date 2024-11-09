from tkinter import *
from RangeSlider import *
from TP2.Models.TP2_2 import *
from TP2.Models.TP2_3 import *
from TP2.Models.TP2_4 import *


def age_analyzer_init(tab):
    """
    Initialize the Variance & Standard Deviation GUI contents.
    :param tab: the master ttk element
    """

    # destroy all children of tab
    for child in tab.winfo_children():
        child.destroy()

    # create a frame to contain all the module's elements
    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)

    # set the title
    ttk.Label(frame, text = "People's Age Analyzer", font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)
    
    # set a label for the data generation module
    ttk.Label(frame, text = 'Generate data:', font = ('Courier', 11, 'bold')).grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = (20, 12))
    
    # number of data to generate
    nb_data_label = ttk.Label(frame, text = 'Number of data')
    nb_data_label.grid(row = 2, column = 0, padx = 5, pady = (8, 0), sticky = E)
    nb_data = IntVar(value = 10)
    spinbox = ttk.Spinbox(frame, from_ = 0, to = 10_000, increment = 1, textvariable = nb_data, width = 5)
    spinbox.grid(row = 2, column = 1, padx = 5, pady = (8, 0), sticky = W)
    
    # range of values
    ttk.Label(frame, text = 'Range').grid(row = 3, column = 0, padx = 5, pady = (0, 5), sticky = SE)
    min_range = DoubleVar(value = 0)
    max_range = DoubleVar(value = 100)
    range_slider = RangeSliderH(frame, [min_range, max_range], min_val = 0, max_val = 120, padX = 17, step_size = 1, font_family = 'Courier', font_size = 9, bgColor = '#f5f6f7', digit_precision = '.0f')
    range_slider.grid(row = 3, column = 1, padx = 5, pady = (0, 5), sticky = W)
    
    # separate the two parts of the form
    ttk.Separator(frame, orient = HORIZONTAL).grid(row = 4, column = 0, columnspan = 2, padx = 150, pady = 12, sticky = EW)

    # create the input elements
    ttk.Label(frame, text = "Ages to analyze:", font = ('Courier', 11, 'bold')).grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = (20, 12))
    values = StringVar()
    format_ = StringVar(value = 'Data Generator')
    entry = ttk.Entry(frame, textvariable = values, width = 25, state = DISABLED)
    entry.grid(row = 6, column = 0, padx = 5, pady = (8, 20), sticky = E)

    # function to disable the entry widget
    def refresh_option(option):
        if option == 'Data Generator':
            entry.config(state = DISABLED)
        else:
            entry.config(state = NORMAL)
    
    ttk.OptionMenu(frame, format_, 'Data Generator', 'Manual CSV','JSON file', 'CSV file', 'Data Generator', 
                   command = refresh_option).grid(row = 6, column = 1, padx = 5, pady = (8, 20), sticky = W)
    
    # set the age groups
    ttk.Label(frame, text = 'Age groups (max value of each group [CSV])').grid(row = 7, column = 0, padx = 5, pady = 20, sticky = E)
    age_groups = StringVar(value = '')
    ttk.Entry(frame, textvariable = age_groups, width = 25).grid(row = 7, column = 1, padx = 5, pady = 20, sticky = W)

    # set the grid configuration of the frame
    frame.grid_columnconfigure(0, weight = 1)
    frame.grid_columnconfigure(1, weight = 1)

    # set the result elements (without displaying them)
    label = ttk.Label(frame, font = ('Courier', 12, 'bold'))
    separator = ttk.Separator(frame, orient = HORIZONTAL)
    image_ctn = ttk.Frame(frame)

    # set the button
    button = ttk.Button(frame, text = 'Analyze', command = lambda: analyze(label, image_ctn, separator, values.get(), format_.get(), age_groups.get(), (nb_data.get(), range_slider.getValues())))
    button.grid(row = 8, column = 0, columnspan = 2, padx = 5, pady = 12)

    # focus on the entry element and bind it to the Enter keys
    spinbox.focus()
    for widget in [entry, spinbox]:
        widget.bind('<Return>', lambda event: button.invoke())
        widget.bind('<KP_Enter>', lambda event: button.invoke())


def analyze(label: ttk.Label, image_ctn: ttk.Frame, separator: ttk.Separator, values: str, format_: str, age_groups:str, generator: tuple):
    """
    Analyzes the given values and displays the results.
    :param label: the label to display
    :param image_ctn: the image to display
    :param separator: the separator to display
    :param values: the values to analyze
    :param format_: the format of the values to analyze
    :param age_groups: the max age of any group contained in the values' range
    :param generator: the parameters to generate data
    """

    # display the elements to show the results
    separator.grid(row = 9, column = 0, columnspan = 2, padx = 5, pady = 20, sticky = EW)
    label.grid(row = 10, column = 0, columnspan = 2, padx = 5, pady = 5)

    arr: list = []
    
    # check the format provided
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
        case 'Data Generator':
            nb_data, ranges = generator
            nb_data = int(nb_data)
            min_range, max_range = int(ranges[0]), int(ranges[1])
            arr = gen_array((nb_data, nb_data), (min_range, max_range))
        case _:
            label.config(text = f'Invalid format: {format_}')
            return

    if len(arr) == 0:
        label.config(text = 'No results found.')
        return

    arr_int: List[int] = []

    # make sure the values are numbers
    for value in arr:
        try:
            arr_int.append(int(value))
        except ValueError:
            label.config(text = 'Invalid format')
            return
    
    # get and parse the age groups
    if age_groups == '':
        age_groups = f'{max(arr_int)}'
    try:
        groups = get_csv_numbers(age_groups, 'int')
    except ValueError as err:
        label.config(text = f'{err}')
        return
    groups.sort()

    # create the age_ranges
    age_ranges: list[tuple] = []
    if min_range:
        min_age: int = min_range
    else:
        min_age = 0

    # format the age groups in a list of tuples to fill the age_ranges variable
    for max_age in groups:
        if max_age == min_age:
            continue
        if max_age > max(arr_int):
            age_ranges.append((min_age, max(arr_int)))
            break
        age_ranges.append((min_age, max_age))
        min_age = max_age + 1
    
    # divide values by age groups
    dict_groups = divide_ranges(arr_int, *age_ranges)
    
    # close all opened graphs
    plt.close('all')
    
    # draw the graph according to the age groups provided
    if len(age_ranges) == 0:
        graph_draw(arr_int, image_ctn)
    else:
        graph_draw(dict_groups, image_ctn)
    
    # get the number of occurrences by age group
    dict_len: dict[tuple[int, int], int] = {}
    for range_ in dict_groups:
        dict_len[range_] = len(dict_groups[range_])
    arr_freq = calc_freq(dict_len)

    # calculate the frequency of each age group in the total list of values
    ranged_freq_arr: List[tuple[Any, List[int], int]] = []
    for range_ in dict_groups:
        ranged_freq: tuple[Any, List[int], int] = (range_, dict_groups[range_], arr_freq[range_])
        ranged_freq_arr.append(ranged_freq)

    # calculate the average, median, variance, standard deviation
    # and the weighted average (according to the frequency of each age group)
    avg = set_precision(average(*arr_int))
    med = set_precision(median(*arr_int))
    var = set_precision(variance(*arr_int))
    stddev = set_precision(std_dev(*arr_int))
    weighted_average = set_precision(weighted_avg(ranged_freq_arr))

    # display the result in the GUI
    label.config(text = f"""
    The average is {avg} and the median is {med}
    The variance is {var} and its standard deviation is {stddev}
    The weighted average is {weighted_average}""")
    image_ctn.grid(row = 11, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = EW)
