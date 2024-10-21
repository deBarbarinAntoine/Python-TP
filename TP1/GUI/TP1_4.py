from tkinter import *
from tkinter import ttk, messagebox
from TP1.Models.TP1_4 import Game
from Utils.Classes import Observer


class GameGUI(Observer):
    def update(self, subject) -> None:
        if self.game.is_ongoing():
            self.game = subject
            self.timer_label.config(text=f'{self.game.timer}')
            self.score_label.config(text=f'Score: {self.game.score}')
            self.current_operation_label.config(text=f'{self.game.current_operation}')
        else:
            self.end_game()

    def answer(self, value):
        try:
            res = int(value)
        except ValueError:
            res = 0
        self.game.answer(res)
        self.answer_entry.delete(0, 'end')
        self.answer_entry.focus()

        

    def end_game(self):
        for child in self.tab.winfo_children():
            child.destroy()

        frame = ttk.Frame(self.tab)
        frame.pack(fill = BOTH, expand = True)
        frame.grid_columnconfigure(0, weight=1)

        self.game.end_game()

        mins, secs = divmod(self.game.total_time, 60)

        ttk.Label(frame, text='Game Over!', font = ('Courier', 14, 'bold')).grid(column = 0, row = 0, padx = 5, pady = 20)

        middle_frame = ttk.Frame(frame)
        middle_frame.grid(column = 0, row = 1, padx = 5, pady = 12)
        
        ttk.Frame(middle_frame).grid(row = 0, column = 0)
        
        inner_frame = ttk.Frame(middle_frame)
        inner_frame.grid(row = 0, column = 1, padx = 5, pady = 5)
        
        ttk.Frame(middle_frame).grid(row = 0, column = 2)
        middle_frame.grid_columnconfigure(0, weight=1)
        middle_frame.grid_rowconfigure(1, weight=2)
        middle_frame.grid_columnconfigure(2, weight=1)
        
        inner_frame.grid_columnconfigure(0, weight=1)
        inner_frame.grid_rowconfigure(1, weight=1)
        
        ttk.Label(inner_frame, text='Name:').grid(column = 0, row = 1, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text='Time:').grid(column = 0, row = 2, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text='Mode:').grid(column = 0, row = 3, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text='Score:').grid(column = 0, row = 4, padx = 20, pady = 5, sticky = W)

        ttk.Label(inner_frame, text=f'{self.game.name}').grid(column = 1, row = 1, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text=f'{mins}:{secs}').grid(column = 1, row = 2, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text=f'{self.game.mode.name}').grid(column = 1, row = 3, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text=f'{self.game.score}').grid(column = 1, row = 4, padx = 20, pady = 5, sticky = W)

        ttk.Button(frame, text='Return', command=lambda : game_init(self.tab)).grid(column = 0, row = 2, padx = 5, pady = 20)


    def __init__(self):
        self.tab = None
        self.game = None
        self.name_label = None
        self.timer_label = None
        self.mode_label = None
        self.score_label = None
        self.current_operation_label = None
        self.answer_entry = None

    @staticmethod
    def new(tab: ttk.Frame, name, timer, mode):
        game_gui: GameGUI = GameGUI()
        game_gui.tab = tab
        mode = Game.Mode(mode)
        game_gui.game = Game.new(name=name, time_sec=timer, mode=mode)
        game_gui.game.attach(game_gui)
        return game_gui


def game_init(tab):
    for child in tab.winfo_children():
        child.destroy()

    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)

    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    
    ttk.Label(frame, text = 'Mental Arithmetic Game', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 20)

    ttk.Label(frame, text="Name:").grid(row = 1, column = 0, sticky = E, padx = 30, pady = 15)
    name = StringVar()
    name_entry = ttk.Entry(frame, textvariable=name)
    name_entry.grid(row = 1, column = 1, sticky = W, padx = 30, pady = 15)

    ttk.Label(frame, text="Timer:").grid(row = 2, column = 0, sticky = E, padx = 30, pady = (15, 0))
    timer = IntVar()
    timer.set(30)
    ttk.Radiobutton(frame, text='30 secs', variable=timer, value=30).grid(row = 2, column = 1, sticky = W, padx = 30, pady = (15, 0))
    ttk.Radiobutton(frame, text='1 min', variable=timer, value=60).grid(row = 3, column = 1, sticky = W, padx = 30)
    ttk.Radiobutton(frame, text='1 min 30 secs', variable=timer, value=90).grid(row = 4, column = 1, sticky = W, padx = 30)
    ttk.Radiobutton(frame, text='2 min', variable=timer, value=120).grid(row = 5, column = 1, sticky = W, padx = 30, pady = (0, 15))

    ttk.Label(frame, text="Mode:").grid(row = 6, column = 0, sticky = E, padx = 30, pady = (15, 0))
    mode = IntVar()
    ttk.Radiobutton(frame, text=Game.Mode.random.name, variable=mode, value=Game.Mode.random.value).grid(row = 6, column = 1, sticky = W, padx = 30, pady = (15, 0))
    ttk.Radiobutton(frame, text=Game.Mode.addition.name, variable=mode, value=Game.Mode.addition.value).grid(row = 7, column = 1, sticky = W, padx = 30)
    ttk.Radiobutton(frame, text=Game.Mode.subtraction.name, variable=mode, value=Game.Mode.subtraction.value).grid(row = 8, column = 1, sticky = W, padx = 30)
    ttk.Radiobutton(frame, text=Game.Mode.multiplication.name, variable=mode, value=Game.Mode.multiplication.value).grid(row = 9, column = 1, sticky = W, padx = 30)
    ttk.Radiobutton(frame, text=Game.Mode.division.name, variable=mode, value=Game.Mode.division.value).grid(row = 10, column = 1, sticky = W, padx = 30, pady = (0, 15))

    ttk.Button(frame, text = 'Top Scores', command = lambda : show_scores(frame)).grid(row = 11, column = 0, padx = 10, pady = 15, sticky = E)
    ttk.Button(frame, text='Start', command=lambda : start(frame, name.get(), timer.get(), mode.get())).grid(row = 11, column = 1, padx = 10, pady = 15, sticky = W)
    
    name_entry.focus()

def show_scores(tab):
    for child in tab.winfo_children():
        child.destroy()

    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)
    frame.grid_columnconfigure(0, weight=1)
    
    game = Game.new()
    top_scores = game.get_top_scores()
    
    if len(top_scores) == 0:
        messagebox.showwarning('Warning', 'No scores available yet!')
        game_init(frame)
        return

    ttk.Label(frame, text = 'Top Scores', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, padx = 5, pady = 20)
    
    inner_frame = ttk.Frame(frame)
    inner_frame.grid(row = 1, column = 0, padx = 5, pady = 20)
    
    i: int = 0
    for score in top_scores:
        if i == 0:
            ttk.Label(inner_frame, text = 'Rank', font = ('Courier', 11, 'bold')).grid(row = i, column = 0, padx = (0, 20), pady = 5, sticky = W)
            ttk.Label(inner_frame, text = f'{'Name':<25}', font = ('Courier', 11, 'bold')).grid(row = i, column = 1, padx = 20, pady = 5, sticky = W)
            ttk.Label(inner_frame, text = f'{'Mode':<15}', font = ('Courier', 11, 'bold')).grid(row = i, column = 2, padx = 20, pady = 5, sticky = W)
            ttk.Label(inner_frame, text = f'{'Time':<5}', font = ('Courier', 11, 'bold')).grid(row = i, column = 3, padx = 20, pady = 5, sticky = W)
            ttk.Label(inner_frame, text = f'{'Score':>10}', font = ('Courier', 11, 'bold')).grid(row = i, column = 4, padx = 20, pady = 5, sticky = E)
            
            ttk.Separator(inner_frame, orient = HORIZONTAL).grid(row = 1, column = 0, columnspan = 5, pady = 5, sticky = EW)
        i += 1
        try:
            time = int(score['time'])
        except ValueError:
            continue
        min, sec = divmod(time, 60)
        timer = f'{min}:{sec}'
        ttk.Label(inner_frame, text = f'{i:2}.').grid(row = i + 1, column = 0, padx = (0, 20), pady = 5, sticky = W)
        ttk.Label(inner_frame, text = f'{score['name']:<25}').grid(row = i + 1, column = 1, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text = f'{score['mode']:<15}').grid(row = i + 1, column = 2, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text = f'{timer:<5}').grid(row = i + 1, column = 3, padx = 20, pady = 5, sticky = W)
        ttk.Label(inner_frame, text = f'{score["score"]:>10}').grid(row = i + 1, column = 4, padx = 20, pady = 5, sticky = E)
    
    button = ttk.Button(frame, text = 'Return', command = lambda : game_init(tab))
    button.grid(row = 2, column = 0, pady = 15)
    frame.focus()
    frame.bind('<Return>', lambda _: game_init(frame))
    frame.bind('<KP_Enter>', lambda _: game_init(frame))
    
    
def start(tab, name, timer, mode):
    if name == '':
        return

    for child in tab.winfo_children():
        child.destroy()

    frame = ttk.Frame(tab)
    frame.pack(fill = BOTH, expand = True)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)
    frame.grid_columnconfigure(3, weight=1)

    game_gui = GameGUI.new(frame, name, timer, mode)

    ttk.Label(frame, text = 'Mental Arithmetic Game', font = ('Courier', 17, 'bold')).grid(row = 0, column = 0, columnspan = 4, padx = 5, pady = 20)

    game_gui.name_label = ttk.Label(game_gui.tab, text=f'Name: {game_gui.game.name}', font = ('Courier', 9, 'bold'))
    game_gui.name_label.grid(column=0, row=1, padx = 5, pady = (20, 0))

    game_gui.timer_label = ttk.Label(game_gui.tab, text=game_gui.game.timer, font = ('Courier', 9, 'bold'))
    game_gui.timer_label.grid(column=1, row=1, padx = 5, pady = (20, 0))

    game_gui.mode_label = ttk.Label(game_gui.tab, text=f'Mode: {game_gui.game.mode.name}', font = ('Courier', 9, 'bold'))
    game_gui.mode_label.grid(column=2, row=1, padx = 5, pady = (20, 0))

    game_gui.score_label = ttk.Label(game_gui.tab, text=f'Score: {game_gui.game.score}', font = ('Courier', 9, 'bold'))
    game_gui.score_label.grid(column=3, row=1, padx = 5, pady = (20, 0))

    ttk.Separator(game_gui.tab, orient='horizontal').grid(column=0, row=2, columnspan=4, sticky = EW, pady = (5, 20))

    game_gui.current_operation_label = ttk.Label(game_gui.tab, text=game_gui.game.current_operation, font = ('Courier', 12, 'bold'))
    game_gui.current_operation_label.grid(column=0, row=3, columnspan=4, padx = 20, pady = 40)

    answer = StringVar()
    game_gui.answer_entry = ttk.Entry(game_gui.tab, textvariable=answer, font = ('Courier', 10, 'normal'))
    game_gui.answer_entry.grid(column=0, row=4, columnspan=4, padx = 20, pady = 40)
    game_gui.answer_entry.focus()
    game_gui.answer_entry.bind(sequence='<Return>', func=lambda e: game_gui.answer(answer.get()))
    game_gui.answer_entry.bind(sequence='<KP_Enter>', func=lambda e: game_gui.answer(answer.get()))

    ttk.Button(game_gui.tab, text='Answer', command=lambda: game_gui.answer(answer.get())).grid(column=1, row=5, columnspan=2, padx = 20, pady = 40)

    game_gui.game.start()