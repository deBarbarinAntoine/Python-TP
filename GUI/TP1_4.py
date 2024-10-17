from tkinter import ttk, StringVar, Text, INSERT, DISABLED, IntVar

from TP1.TP1_4 import Game
from Utils.Classes import Observer


class GameGUI(Observer):
    def update(self, subject) -> None:
        if self.game.is_ongoing():
            self.game = subject
            self.timer_label.config(text=f'{self.game.timer}')
            self.score_label.config(text=f'{self.game.score}')
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

        self.game.end_game()

        mins, secs = divmod(self.game.total_time, 60)

        ttk.Label(self.tab, text='Game Over!').grid(column=3, row=0, columnspan=2)

        ttk.Label(self.tab, text=f'Name: {self.game.name}').grid(column=2, row=2, columnspan=4)
        ttk.Label(self.tab, text=f'Time: {mins}:{secs}').grid(column=2, row=3, columnspan=4)
        ttk.Label(self.tab, text=f'Mode: {self.game.mode.name}').grid(column=2, row=4, columnspan=4)
        ttk.Label(self.tab, text=f'Score: {self.game.score}').grid(column=2, row=5, columnspan=4)

        ttk.Button(self.tab, text='Return', command=lambda : game_init(self.tab)).grid(column=3, row=7, columnspan=2)


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
    def new(tab: ttk.Notebook, name, timer, mode):
        game_gui: GameGUI = GameGUI()
        game_gui.tab = tab
        mode = Game.Mode(mode)
        game_gui.game = Game.new(name=name, time_sec=timer, mode=mode)
        game_gui.game.attach(game_gui)
        return game_gui


def game_init(tab):
    for child in tab.winfo_children():
        child.destroy()

    ttk.Label(tab, text="Name:").grid(column=3, row=0, columnspan=2)
    name = StringVar()
    ttk.Entry(tab, textvariable=name).grid(column=2, row=1, columnspan=4)

    ttk.Label(tab, text="Timer:").grid(column=3, row=2, columnspan=2)
    timer = IntVar()
    timer.set(30)
    ttk.Radiobutton(tab, text='30 secs', variable=timer, value=30).grid(column=2, row=3)
    ttk.Radiobutton(tab, text='1 min', variable=timer, value=60).grid(column=3, row=3)
    ttk.Radiobutton(tab, text='1 min 30 secs', variable=timer, value=90).grid(column=4, row=3)
    ttk.Radiobutton(tab, text='2 min', variable=timer, value=120).grid(column=5, row=3)

    ttk.Label(tab, text="Mode:").grid(column=3, row=4, columnspan=2)
    mode = IntVar()
    ttk.Radiobutton(tab, text=Game.Mode.random.name, variable=mode, value=Game.Mode.random.value).grid(column=2, row=5)
    ttk.Radiobutton(tab, text=Game.Mode.addition.name, variable=mode, value=Game.Mode.addition.value).grid(column=3, row=5)
    ttk.Radiobutton(tab, text=Game.Mode.subtraction.name, variable=mode, value=Game.Mode.subtraction.value).grid(column=4, row=5)
    ttk.Radiobutton(tab, text=Game.Mode.multiplication.name, variable=mode, value=Game.Mode.multiplication.value).grid(column=5, row=5)
    ttk.Radiobutton(tab, text=Game.Mode.division.name, variable=mode, value=Game.Mode.division.value).grid(column=6, row=5)

    ttk.Button(tab, text='Start', command=lambda : start(tab, name.get(), timer.get(), mode.get())).grid(column=2, row=6, columnspan=4)

def start(tab, name, timer, mode):
    if name == '':
        return

    for child in tab.winfo_children():
        child.destroy()

    game_gui = GameGUI.new(tab, name, timer, mode)

    game_gui.name_label = ttk.Label(game_gui.tab, text=game_gui.game.name)
    game_gui.name_label.grid(column=2, row=0)

    game_gui.timer_label = ttk.Label(game_gui.tab, text=game_gui.game.timer)
    game_gui.timer_label.grid(column=3, row=0)

    game_gui.mode_label = ttk.Label(game_gui.tab, text=game_gui.game.mode.name)
    game_gui.mode_label.grid(column=4, row=0)

    game_gui.score_label = ttk.Label(game_gui.tab, text=game_gui.game.score)
    game_gui.score_label.grid(column=5, row=0)

    ttk.Separator(game_gui.tab, orient='horizontal').grid(column=2, row=1, columnspan=4)

    game_gui.current_operation_label = ttk.Label(game_gui.tab, text=game_gui.game.current_operation)
    game_gui.current_operation_label.grid(column=2, row=3, columnspan=4)

    answer = StringVar()
    game_gui.answer_entry = ttk.Entry(game_gui.tab, textvariable=answer)
    game_gui.answer_entry.grid(column=2, row=5, columnspan=4)
    game_gui.answer_entry.focus()
    game_gui.answer_entry.bind(sequence='<Return>', func=lambda e: game_gui.answer(answer.get()))

    ttk.Button(game_gui.tab, text='Answer', command=lambda: game_gui.answer(answer.get())).grid(column=3, row=6, columnspan=2)

    game_gui.game.start()