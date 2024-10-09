from tkinter import ttk
from ttkthemes import ThemedTk
from GUI.TP1_1 import temp_init
from GUI.TP1_2 import num_init
from GUI.TP1_3 import greet_init


def main_window():
    window = ThemedTk(theme="breeze")
    window.geometry('800x450')
    window.title('TP Python - Antoine de Barbarin')
    tab_control = ttk.Notebook(window)
    tab_control.grid(column=0, row=0, sticky='nsew')
    tab_tp1 = ttk.Frame(tab_control)
    tab_tp2 = ttk.Frame(tab_control)
    tab_tp3 = ttk.Frame(tab_control)
    tab_control.add(tab_tp1, text='TP 1')
    tab_control.add(tab_tp2, text='TP 2')
    tab_control.add(tab_tp3, text='TP 3')
    frame = ttk.Frame(tab_tp1)
    ttk.Button(tab_tp1, text='Temperature Converter', command=lambda: temp_init(frame), padding='10').grid(column = 0, row = 0, padx = 30, pady = 30)
    ttk.Button(tab_tp1, text='Sum and Product of Even Numbers', command=lambda: num_init(frame), padding='10').grid(column = 0, row = 1, padx = 30, pady = 30)
    ttk.Button(tab_tp1, text='Welcome Message Generator', command=lambda: greet_init(frame), padding='10').grid(column = 0, row = 2, padx = 30, pady = 30)
    ttk.Separator(tab_tp1, orient='vertical').grid(column = 1, row = 0, padx = 30, pady = 30, sticky='ns')
    frame.grid(column = 2, row = 0, sticky = 'nsew')
    tab_control.pack(expand=1, fill='both', side='top')
    window.mainloop()

if __name__ == '__main__':
    main_window()