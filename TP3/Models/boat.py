class Boat:
    """
    Class representing a boat.
    """
    def __init__(self, name: str, length: int | float, capacity: int, passengers: int = 0):
        """
        Boat constructor.
        :param name: the name of the boat
        :param length: the length of the boat
        :param capacity: the maximum capacity of the boat
        :param passengers: the passengers of the boat
        """
        self.name: str = name
        self.length: int | float = length
        self.capacity: int = capacity
        if passengers > capacity: passengers = capacity
        self.passengers: int = passengers

    def _free_space(self) -> int:
        """
        Calculates the free space of the boat.
        :return: the free space of the boat
        """
        return self.capacity - self.passengers

    def add_passengers(self, passengers: int = 1) -> bool:
        """
        Adds passengers to the boat.
        :param passengers: the number of passengers to add to the boat (default 1)
        :return: true if the passengers were added to the boat, false otherwise
        """
        if passengers > self._free_space() or passengers < 1:
            return False
        self.passengers += passengers
        return True

    def remove_passengers(self, passengers: int = -1) -> None:
        """
        Removes passengers from the boat.
        :param passengers: the number of passengers to remove from the boat (default: all passengers)
        :return: None
        """
        if passengers == -1 or passengers > self.passengers:
            self.passengers = 0
        elif passengers > 0:
            self.passengers -= passengers

    def navigate(self) -> None:
        """
        Makes the boat navigate.
        :return: None
        """
        print(f'Boat {self.name} is navigating...⛵')

    def display_info(self, to_stdout: bool = False) -> str:
        """
        Displays information about the boat.
        :param to_stdout: whether to print the result in the stdout or not.
        :return: the string containing the information about the boat.
        """
        if to_stdout:
            print(self)
        return self.__str__()

    def __str__(self) -> str:
        return f"""
##################################################
Boat: {self.name}
Length: {self.length:2}m
Max capacity: {self.capacity}
Current passengers: {self.passengers}
##################################################
"""
