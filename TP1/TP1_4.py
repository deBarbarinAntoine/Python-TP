import json
import threading
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
        pass

    def detach(self, observer: Observer) -> None:
        """
        :param observer:
        """
        self._observers.remove(observer)
        pass

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
        pass

    def __init__(self):
        self.name = 'Player'
        self.mode = Game.Mode.random
        self.total_time = 30
        self.timeout = self.total_time
        self.score = 0
        self.timer = '00:30'
        self.current_operation: str
        self.current_result: int
        self.answer: str
        self._timer_thread = threading.Thread(target=self.countdown, daemon=True)
        self._observers: List[Utils.Classes.Observer] = []

    def is_ongoing(self) -> bool:
        return self._timer_thread.is_alive()

    class Mode(Enum):
        random = 0
        addition = 1
        subtraction = 2
        multiplication = 3
        division = 4

    @staticmethod
    def new(name = 'Player', mode = Mode.random, time_sec = 30):
        new_game = Game()
        new_game.name = name
        new_game.mode = mode
        new_game.timeout = time_sec
        return new_game

    def countdown(self):
        while self.timeout:
            mins, secs = divmod(self.timeout, 60)
            self.timer = '{:02d}:{:02d}'.format(mins, secs)
            time.sleep(1)
            self.timeout -= 1

    def new_operation(self):
        if self.mode == Game.Mode.random:
            mode = Game.Mode(random.randint(1, 4))
        else:
            mode = self.mode
        match mode:
            case self.Mode.addition:
                max1, max2 = 100, 100
                op = '+'
                def operation(a, b):
                    return a + b
            case self.Mode.subtraction:
                max1, max2 = 100, 100
                op = '-'
                def operation(a, b):
                    return a - b
            case self.Mode.multiplication:
                max1, max2 = 30, 15
                op = 'x'
                def operation(a, b):
                    return a * b
            case self.Mode.division:
                max1, max2 = 100, 15
                op = '÷'
                def operation(a, b):
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

        return f'{num1} {op} {num2}', operation(num1, num2)

    def end_game(self):
        score_entry = {'name': self.name, 'mode': self.mode.name, 'time': self.total_time, 'score': self.score}
        all_scores = json.JSONDecoder().decode(open('../Assets/scores.json').read())
        all_scores.append(score_entry)
        json_object = json.dumps(all_scores, indent=4)
        with open('../Assets/scores.json', 'w') as file:
            file.write(json_object)

    def play(self):
        while self._timer_thread.is_alive():
            self.answer = ''
            self.current_operation, self.current_result = self.new_operation()
            print(f'self.current_operation: {self.current_operation}, self.current_result: {self.current_result}')
            while self.answer == '':
                time.sleep(0.1)
            try:
                answer = int(self.answer)
            except ValueError:
                self.score -= 1
            else:
                if answer == self.current_result:
                    self.score += 1
                else:
                    self.score -= 1
        self.end_game()

    def start(self):
        self._timer_thread.start()
        game_thread = threading.Thread(target=self.play, daemon=True)
        game_thread.start()

if __name__ == '__main__':
    game = Game.new()
    game.start()

    while game.is_ongoing():
        print(f'Time left: {game.timeout}')
        print(f'Score: {game.score}')
        print(f'Operation: {game.current_operation}')
        print("Enter your answer:")
        game.answer = input('> ')
    print(game.score)
