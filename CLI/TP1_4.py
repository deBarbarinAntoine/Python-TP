import re
from typing import List

import Utils
from Utils import Classes
from TP1 import TP1_4
from Utils.Classes import Colors


class MathGameCLI(Utils.Classes.Observer):

    def update(self, subject: TP1_4.Game) -> None:
        self.game = subject
        self.refresh()

    def refresh(self):
        if self.game.is_ongoing():
            width = len(f'{self.game.name}    {self.game.timer}    {self.game.score} pts ┃ X ESC')
            self.board = f"""{self.game.name}    {self.game.timer}    {self.game.score} pts ┃ X ESC
{'▔' * width}
{self.game.current_operation:^{width}}

> {self.buffer}"""
        else:
            self.game.end_game()
            self.board = f"""
        \tGAME OVER!

          Name: {self.game.name}
          Timer: {self.game.total_time}
          Score: {self.game.score}
          Mode: {self.game.mode.name}"""

        Utils.clear()
        print(self.board)

    def __init__(self):
        self.board: List[str] = []
        self.buffer = ''
        self.is_interrupted = False
        self.game: TP1_4.Game = TP1_4.Game.new()

    @staticmethod
    def new():
        return MathGameCLI()


def cli():
    main_menu = Utils.Classes.MenuCLI.new(
        'New Game', 'Scores',
        title='Mental Arithmetic Game',
        exit_option='Return'
    )
    match main_menu.run():
        case 0:
            return
        case 1:
            begin_game()
        case 2:
            scores()

def scores():
    game = TP1_4.Game.new()
    top_scores = game.get_top_scores()
    width = len(f'Rank  {' '*25}  {' '*15}  {' '*5}  {' '*10}')
    print(f'{'TOP SCORES':^{width}}')
    print('▔' * width)
    print(f'{Colors.BOLD}{Colors.UNDERLINE}Rank  {'Name':<25}  {'Mode':<15}  {'Time':<5}  {'Score':>10}{Colors.END}')
    i: int = 0
    for score in top_scores:
        i += 1
        try:
            time = int(score['time'])
        except ValueError:
            continue
        min, sec = divmod(time, 60)
        timer = f'{min}:{sec}'
        print(f'{i:2}.   {score['name']:<25}  {score['mode']:<15}  {timer:<5}  {score["score"]:>10}')
    print()
    print(f'Type [Enter] to continue')
    input()

def setup():
    name: str = 'Player'
    timer: int = 30
    mode: TP1_4.Game.Mode = TP1_4.Game.Mode.random
    while True:
        print("Enter your name:")
        name = input("> ")
        name = name.strip()
        if name != '':
            break
    timer_menu = Utils.Classes.MenuCLI.new(
        "30 seconds", "1 minute", "1 minute 30 seconds", "2 minutes",
        title="Timer:",
        exit_option='Return'
    )
    match timer_menu.run():
        case 0:
            return None, False
        case 1:
            timer = 30
        case 2:
            timer = 60
        case 3:
            timer = 90
        case 4:
            timer = 120
    mode_menu = Utils.Classes.MenuCLI.new(
        "Random operations", "Additions", "Subtractions", "Multiplications", "Divisions",
        title="Choose your game mode:",
        exit_option="Return"
    )
    match mode_menu.run():
        case 0:
            return False
        case 1:
            mode = TP1_4.Game.Mode.random
        case 2:
            mode = TP1_4.Game.Mode.addition
        case 3:
            mode = TP1_4.Game.Mode.subtraction
        case 4:
            mode = TP1_4.Game.Mode.multiplication
        case 5:
            mode = TP1_4.Game.Mode.division
    return TP1_4.Game.new(name, mode, timer), True


def begin_game():
    game, ok = setup()
    if ok:
        cli_game = MathGameCLI.new()
        game.attach(cli_game)
        game.start()
        while game.is_ongoing():
            keyboard_io = Utils.Classes.KeyboardIO.new(obj = cli_game, authorized_regex = re.compile(r'[\d-]'))
            buffer = keyboard_io.get_input()
            if cli_game.is_interrupted:
                game.detach(cli_game)
                game.stop()
                break
            try:
                answer: int = int(buffer)
            except ValueError:
                answer: int = 0
            game.answer(answer)
            cli_game.buffer = ''
            cli_game.refresh()
