try:
    from TP3.Models.boat import Boat
except ImportError:
    from boat import Boat


class Port:
    """
    Class representing a port.
    """
    def __init__(self, name: str):
        """
        Port constructor.
        :param name: the name of the port.
        """
        self.name: str = name
        self.boats: list[Boat] = []

    def add_boat(self, boat: Boat) -> None:
        """
        Adds a boat to the port.
        :param boat: the boat to add.
        :return: None
        """
        self.boats.append(boat)

    def remove_boat(self, boat: Boat) -> None:
        """
        Removes a boat from the port.
        :param boat: the boat to remove.
        :return: None
        """
        try:
            self.boats.remove(boat)
        except ValueError:
            pass

    def navigate_all(self) -> None:
        """
        Makes all boats in the port navigate.
        :return: None
        """
        for boat in self.boats:
            boat.navigate()

    def display_boats(self, to_stdout: bool = False) -> str:
        """
        Displays the port's boats.
        :param to_stdout: whether to print the result in the stdout or not.
        :return: the string containing the port's boats.
        """
        if to_stdout:
            print(self)
        return self.__str__()

    def __str__(self) -> str:
        buffer: str = ""
        for boat in self.boats:
            buffer += str(boat) + "\n"
        return buffer