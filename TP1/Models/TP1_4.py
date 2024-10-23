import json
from threading import Thread
import time
from enum import Enum
import Utils
from Utils import *


class Game(Utils.Classes.Subject):
    """
    Represents a mental arithmetic game with customizable modes and scoring.

    This class inherits from the Observer pattern's `Subject` class to allow
    observers to be notified of game events.
    """

    def attach(self, observer: Observer) -> None:
        """
        Adds an observer to the Game object.
        :param observer: the Observer to be added to the Game object
        """
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the Game object.
        :param observer: the Observer to be removed from the Game object
        """
        self._observers.remove(observer)

    def notify(self) -> None:
        """
        Notifies all attached observers of game updates. This is called
        whenever the game state changes.
        """
        for observer in self._observers:
            observer.update(self)

    def __init__(self):
        """
        Initializes a new Game object.

        Sets default values for game properties, including player name, mode,
        total time, score, timer display format, current operation, observers list,
        score file path, and a timer thread.
        """
        self.name: str = 'Player'
        self.mode: Game.Mode = Game.Mode.random
        self.total_time: int = 30
        self.timeout: int = self.total_time
        self.score: int = 0
        self.timer: str = '00:30'
        self.current_operation: str = ''
        self.current_result: int = 0
        self._timer_thread: Thread = Thread(target=self.countdown, daemon=True)
        self._timer_stop_signal: bool = False
        self._observers: List[Utils.Classes.Observer] = []
        self._score_file: str = 'Data/scores.json'

    def is_ongoing(self) -> bool:
        """
        Checks if the game is still ongoing.
        :return: True if the timeout is greater than 0, False otherwise.
        """
        return self.timeout > 0

    class Mode(Enum):
        """
        Enumeration representing the available game modes.
        """
        random = 0
        addition = 1
        subtraction = 2
        multiplication = 3
        division = 4

    @staticmethod
    def new(name = 'Player', mode = Mode.random, time_sec = 30, score_file = 'Data/scores.json'):
        """
        Creates a new Game object with the specified parameters.
        :param name: the name of the player
        :param mode: the game mode
        :param time_sec: the duration of the game in seconds
        :param score_file: the score file path
        :return: the new Game object
        """
        new_game = Game()
        new_game.name = name
        new_game.mode = mode
        new_game.timeout = time_sec
        new_game._score_file = score_file
        return new_game

    def countdown(self) -> None:
        """
        Runs a countdown timer thread that updates the timer display and
        notifies observers every second. Stops when the timeout reaches 0
        or the stop signal is set.

        This method runs in a separate thread to avoid blocking the main thread.
        """
        while self.timeout:
            mins, secs = divmod(self.timeout, 60)
            self.timer = '{:02d}:{:02d}'.format(mins, secs)
            self.notify()
            time.sleep(1)
            
            # checking if there is a _timer_stop_signal
            if self._timer_stop_signal:
                # exit the timer and terminate the thread
                return
            self.timeout -= 1
            
        # notify the attached Observer
        self.notify()

    def new_operation(self) -> None:
        """
        Generates a new operation according to the game mode selected beforehand.
        
        Refreshes `self.current_operation` and `self.current_result`.
        
        :raise ValueError: if the game mode is invalid.
        """
        
        # if the game mode is random, select a random operation
        if self.mode == Game.Mode.random:
            mode = Game.Mode(random.randint(1, 4))
        else:
            mode = self.mode
        
        # generate the maximum value of both operands
        # and the operation function according to the selected operation
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
                
            # raise a ValueError if mode is not in the accepted range
            case _:
                raise ValueError(f'Invalid mode {mode}')

        # setting the first operand
        num1 = random.randint(1, max1)
        
        # generation of the 2nd operand if the operation is a division
        if mode == Game.Mode.division:
            while True:
                
                # getting the divisors of num1 between 2 and 15
                divisors = Utils.trim_min_max(Utils.get_divisors(num1), 2, 16)
                
                if len(divisors) > 0:
                    
                    # selecting a random divisor as the second operand
                    num2 = random.choice(divisors)
                    break
                    
                # generate another first operand if there are no divisor found    
                num1 = random.randint(1, max1)
        else:
            # randomly generate a second operand
            num2 = random.randint(1, max2)

        # assigning new values to self.current_operation and self.current_result
        self.current_operation, self.current_result = f'{num1} {op} {num2}', operation(num1, num2)

    def end_game(self) -> None:
        """
        Ends the game by saving the score in the JSON score file.
        """
        score_entry = {'name': self.name, 'mode': self.mode.name, 'time': self.total_time, 'score': self.score}
        all_scores = json.JSONDecoder().decode(open(self._score_file).read())
        all_scores.append(score_entry)
        json_object = json.dumps(all_scores, indent=4)
        
        with open(self._score_file, 'w') as file:
            file.write(json_object)

    def get_scores(self):
        """
        Gets the scores from the JSON score file and sort them by score, time, name and mode.
        :return: the sorted list of scores or [] if no scores were found.
        """
        try:
            scores: list = json.JSONDecoder().decode(open(self._score_file).read())
            
        except FileNotFoundError or json.decoder.JSONDecodeError or ValueError:
            return []
        
        # sort by descending mode
        scores.sort(key=lambda x: x['mode'], reverse=True)

        # sort by ascending name
        scores.sort(key=lambda x: x['name'], reverse=False)

        # sort by descending time
        scores.sort(key=lambda x: x['time'], reverse=True)

        # sort by descending score
        scores.sort(key=lambda x: x['score'], reverse=True)
        
        return scores

    def get_top_scores(self):
        """
        Gets the 10 top scores from the JSON score file and sort them by score, time, name, mode.
        :return: the sorted list of top scores or [] if no scores were found.
        """
        scores = self.get_scores()
        return scores[:10]

    def answer(self, answer: int) -> None:
        """
        If the game is still ongoing, provide an answer to the current_operation, updates the score accordingly
        and generates a new operation.
        :param answer: the answer
        """
        if self.is_ongoing():
            
            if answer == self.current_result:
                self.score += 1
            else:
                self.score -= 1
                
            self.new_operation()
            
        self.notify()

    def start(self) -> None:
        """
        Starts the game.
        :raise ValueError: if there are no `Observer` attached.
        """
        
        if len(self._observers) < 1:
            raise ValueError('No observers defined')
        
        # generate a new operation
        self.new_operation()
        
        # start the timer thread
        self._timer_thread.start()
        
        # notify the attached Observer
        self.notify()

    def stop(self):
        """
        Stops the game.
        """
        self._timer_stop_signal = True
        