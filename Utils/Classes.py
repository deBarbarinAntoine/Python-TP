from abc import ABC, abstractmethod
import re
from pynput import keyboard
from pynput.keyboard import Key

from Utils import take_int, clear

class Colors:
    """
    The class Colors provides a way of defining a color in the terminal.
    """
    BLUE = '\033[94m'
    CYAN = '\033[38;2;0;255;255m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject) -> None:
        """
        Receive update from subject.
        """
        pass


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class KeyboardIO:
    """
    The KeyboardIO class is a way to handle keyboard output and put it in a buffer.
    """

    def __init__(self):
        self.obj = None
        self.delimiter: Key = Key.enter
        self.authorized_regex: re.Pattern = re.compile('[ -~]')
        self._listener = keyboard.Listener(
            on_press=self._on_key_press,
            suppress=True)
        self._refresh_fn = None

    @staticmethod
    def new(obj=None, delimiter=Key.enter, authorized_regex=re.compile('[ -~]'), suppress_output=True, refresh_fn=None):
        """
        The static method new is a public constructor to make a KeyboardIO instance.

        :param obj: the object holding the buffer (needs a buffer attribute).
        :param delimiter: the Key which once pressed, will end the listener method and return the buffer.
        :param authorized_regex: a regex re.Pattern with the characters to accept in the buffer.
        :param suppress_output: whether to suppress the output of the keyboard or not.
        :param refresh_fn: a callback function to refresh the display with the updated buffer (can also be included in the obj parameter as the obj.refresh() method).
        :return: the buffer once the delimiter Key has been pressed.
        """
        keyboard_io = KeyboardIO()
        if obj is not None and hasattr(obj, 'buffer'):
            keyboard_io.obj = obj
        keyboard_io.delimiter = delimiter
        keyboard_io.authorized_regex = authorized_regex
        keyboard_io._listener = keyboard.Listener(
            on_press=keyboard_io._on_key_press,
            suppress=suppress_output
        )
        if refresh_fn is not None:
            keyboard_io._refresh_fn = refresh_fn
        elif hasattr(obj, 'refresh') and callable(obj.refresh):
            keyboard_io._refresh_fn = obj.refresh
        return keyboard_io

    def get_input(self) -> str:
        """
        The get_input method starts the listener and gets the input from the keyboard.
        :return: the buffer once the delimiter Key has been pressed.
        """
        self._listener.start()
        self._listener.join()
        return self.obj.buffer

    def _on_key_press(self, key):
        """
        The _on_key_press method is called whenever a key is pressed.
        :param key: the delimiter Key that will stop the listener.
        :return: None.
        """
        if key == self.delimiter:
            self._listener.stop()
        elif key == Key.backspace:
            self.obj.buffer = self.obj.buffer[:-1]
        elif key == Key.esc:
            if hasattr(self.obj, 'is_interrupted'):
                self.obj.is_interrupted = True
                self._listener.stop()
        elif hasattr(key, "char") and self.authorized_regex.match(key.char):
            self.obj.buffer += key.char
            if self._refresh_fn is not None and callable(self._refresh_fn):
                self._refresh_fn()

class MenuCLI:
    """
    The Menu class provides a way of handling a simple menu in CLI.
    """
    def __init__(self):
        self._title = ''
        self._options = []
        self._exit_option = None
        self._width_max = 0

    @staticmethod
    def new(*options, title = 'Menu', exit_option = None):
        """
        The new method creates a new menu object.
        :param options: the list of options available in the menu.
        :param title: the title of the menu.
        :param exit_option: the label of the exit option.
        :return: the new menu object.
        """
        menu = MenuCLI()
        menu._options = options
        menu._title = title
        menu._width_max = len(title)
        i: int = 0
        for option in options:
            i += 1
            if len(f'{i}/ {option}') > menu._width_max:
                menu._width_max = len(f'{i}/ {option}')
        if exit_option is not None:
            menu._exit_option = exit_option
        return menu

    def run(self) -> int:
        """
        The run method starts the menu.
        :return: the integer associated with the option chosen by the user.
        """
        clear()
        print(f'{Colors.BOLD}{self._title:^{self._width_max}}{Colors.END}')
        print('▔' * self._width_max)
        i: int = 0
        for option in self._options:
            i += 1
            print(f'{i}/ {option}')
        exit_label = 'Exit'
        if self._exit_option is not None:
            exit_label = self._exit_option
        print(f'{Colors.RED}0/ {exit_label}{Colors.END}')
        while True:
            res = take_int('> ')
            if 0 <= res <= len(self._options):
                return res
