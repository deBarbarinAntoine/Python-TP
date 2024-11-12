import unittest
from io import StringIO
from unittest import TestCase, TestLoader, TextTestRunner
from unittest.mock import patch

try:
    from TP3.Models.boat import Boat
except ImportError:
    from boat import Boat


class TestBoat(TestCase):
    def test__free_space(self):
        boat = Boat("test", 4.2, 8, 2)
        self.assertIsNotNone(boat)
        self.assertEqual(boat._free_space(), 6)

    def test_add_passengers(self):
        boat = Boat("test", 3, 10, 4)
        self.assertIsNotNone(boat)
        self.assertEqual(boat.passengers, 4)

        ok = boat.add_passengers()
        self.assertTrue(ok)
        self.assertEqual(boat.passengers, 5)

        ok = boat.add_passengers(-1)
        self.assertFalse(ok)
        self.assertEqual(boat.passengers, 5)

        ok = boat.add_passengers(2)
        self.assertTrue(ok)
        self.assertEqual(boat.passengers, 7)

        ok = boat.add_passengers(4)
        self.assertFalse(ok)
        self.assertEqual(boat.passengers, 7)

        ok = boat.add_passengers(3)
        self.assertTrue(ok)
        self.assertEqual(boat.passengers, 10)

        ok = boat.add_passengers()
        self.assertFalse(ok)
        self.assertEqual(boat.passengers, 10)

    def test_remove_passengers(self):
        boat = Boat("test", 6.74, 16, 16)
        self.assertIsNotNone(boat)
        self.assertEqual(boat.passengers, 16)

        boat.remove_passengers(1)
        self.assertEqual(boat.passengers, 15)

        boat.remove_passengers(-2)
        self.assertEqual(boat.passengers, 15)

        boat.remove_passengers(4)
        self.assertEqual(boat.passengers, 11)

        boat.remove_passengers()
        self.assertEqual(boat.passengers, 0)

        boat.remove_passengers(3)
        self.assertEqual(boat.passengers, 0)

    def test_navigate(self):
        boat = Boat("test", 6.74, 16, 16)
        self.assertIsNotNone(boat)
        with patch('sys.stdout', new = StringIO()) as fake_out:
            boat.navigate()
            self.assertEqual(fake_out.getvalue(), f'Boat {boat.name} is navigating...⛵\n')

def test_boat_run() -> str:
    test = TestLoader().loadTestsFromTestCase(TestBoat)
    with patch('sys.stdout', new_callable = StringIO) as fake_out:
        TextTestRunner(stream=fake_out, verbosity=2).run(test)
        result = fake_out.getvalue()
        return result

if __name__ == '__main__':
    print(test_boat_run())