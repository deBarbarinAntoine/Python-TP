import json
from threading import Thread
import time
from enum import Enum
import random
from typing import List

import Utils
from Utils import Classes
from Utils.Classes import Observer


class Game(Utils.Classes.Subject):

    def attach(self, observer: Observer) -> None:
        """
        :param observer:
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        :param observer:
        """
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def __init__(self):
        self.name: str = 'Player'
        self.mode: Game.Mode = Game.Mode.random
        self.total_time: int = 30
        self.timeout: int = self.total_time
        self.score: int = 0
        self.timer: str = '00:30'
        self.current_operation: str = ''
        self.current_result: int = 0
        self._timer_process: Thread = Thread(target=self.countdown, daemon=True)
        self._timer_stop_signal: bool = False
        self._observers: List[Utils.Classes.Observer] = []
        self._score_file: str = 'Data/scores.json'

    def is_ongoing(self) -> bool:
        return self.timeout > 0

    class Mode(Enum):
        random = 0
        addition = 1
        subtraction = 2
        multiplication = 3
        division = 4

    @staticmethod
    def new(name = 'Player', mode = Mode.random, time_sec = 30, score_file = 'Data/scores.json'):
        new_game = Game()
        new_game.name = name
        new_game.mode = mode
        new_game.timeout = time_sec
        new_game._score_file = score_file
        return new_game

    def countdown(self) -> None:
        while self.timeout:
            mins, secs = divmod(self.timeout, 60)
            self.timer = '{:02d}:{:02d}'.format(mins, secs)
            self.notify()
            time.sleep(1)
            if self._timer_stop_signal:
                return
            self.timeout -= 1
        self.notify()

    def new_operation(self) -> None:
        if self.mode == Game.Mode.random:
            mode = Game.Mode(random.randint(1, 4))
        else:
            mode = self.mode
        match mode:
            case self.Mode.addition:
                max1, max2 = 100, 100
                op = '+'
                def operation(a: int, b: int) -> int:
                    return a + b
            case self.Mode.subtraction:
                max1, max2 = 100, 100
                op = '-'
                def operation(a: int, b: int) -> int:
                    return a - b
            case self.Mode.multiplication:
                max1, max2 = 30, 15
                op = 'x'
                def operation(a: int, b: int) -> int:
                    return a * b
            case self.Mode.division:
                max1, max2 = 100, 15
                op = '÷'
                def operation(a: int, b: int) -> int:
                    return a / b
            case _:
                raise ValueError(f'Invalid mode {mode}')

        num1 = random.randint(1, max1)

        if mode == Game.Mode.division:
            while True:
                divisors = Utils.trim_min_max(Utils.get_divisors(num1), 1, 16)
                if len(divisors) > 0:
                    num2 = random.choice(divisors)
                    break
                num1 = random.randint(1, max1)
        else:
            num2 = random.randint(1, max2)

        self.current_operation, self.current_result = f'{num1} {op} {num2}', operation(num1, num2)

    def end_game(self) -> None:
        score_entry = {'name': self.name, 'mode': self.mode.name, 'time': self.total_time, 'score': self.score}
        all_scores = json.JSONDecoder().decode(open(self._score_file).read())
        all_scores.append(score_entry)
        json_object = json.dumps(all_scores, indent=4)
        with open(self._score_file, 'w') as file:
            file.write(json_object)

    def get_scores(self):
        try:
            scores: list = json.JSONDecoder().decode(open(self._score_file).read())
        except FileNotFoundError or json.decoder.JSONDecodeError or ValueError:
            return []
        scores.sort(key=lambda x: x['mode'], reverse=True)
        scores.sort(key=lambda x: x['name'], reverse=False)
        scores.sort(key=lambda x: x['time'], reverse=True)
        scores.sort(key=lambda x: x['score'], reverse=True)
        return scores

    def get_top_scores(self):
        scores = self.get_scores()
        return scores[:10]

    def answer(self, answer: int) -> None:
        if self.is_ongoing():
            if answer == self.current_result:
                self.score += 1
            else:
                self.score -= 1
            self.new_operation()
        self.notify()

    def start(self) -> None:
        if len(self._observers) < 1:
            raise ValueError('No observers defined')
        self.new_operation()
        self._timer_process.start()
        self.notify()

    def stop(self):
        self._timer_stop_signal = True
