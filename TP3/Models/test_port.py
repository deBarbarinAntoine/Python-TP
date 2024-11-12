from io import StringIO
import unittest
from unittest import TestCase, TestLoader, TextTestRunner
from unittest.mock import patch

try:
    from TP3.Models.boat import Boat
    from TP3.Models.port import Port
except ImportError:
    from boat import Boat
    from port import Port


class TestPort(TestCase):
    def test_add_boat(self):
        port = Port("test-port")
        self.assertIsNotNone(port)

        boat1 = Boat("boat1", 1, 2, 1)
        self.assertIsNotNone(boat1)

        port.add_boat(boat1)
        self.assertIn(boat1, port.boats)

        boat2 = Boat("boat2", 1.5, 3, 2)
        self.assertIsNotNone(boat2)

        port.add_boat(boat2)
        self.assertIn(boat2, port.boats)

    def test_remove_boat(self):
        port = Port("test-port")
        self.assertIsNotNone(port)

        boat1 = Boat("boat1", 1, 2, 1)
        boat2 = Boat("boat2", 1.5, 3, 2)

        port.add_boat(boat1)
        port.add_boat(boat2)

        self.assertIn(boat1, port.boats)
        self.assertIn(boat2, port.boats)

        port.remove_boat(boat1)
        self.assertNotIn(boat1, port.boats)

        port.remove_boat(boat2)
        self.assertNotIn(boat2, port.boats)
        self.assertEqual(port.boats, [])

        port.remove_boat(boat1)
        self.assertEqual(port.boats, [])

        port.remove_boat(boat2)
        self.assertEqual(port.boats, [])

    def test_navigate_all(self):
        port = Port("test-port")
        self.assertIsNotNone(port)

        boat1 = Boat("boat1", 1, 2, 1)
        boat2 = Boat("boat2", 1.5, 3, 2)

        port.add_boat(boat1)
        port.add_boat(boat2)

        with patch('sys.stdout', new = StringIO()) as fake_out:
            port.navigate_all()
            self.assertEqual(fake_out.getvalue(), f'Boat {boat1.name} is navigating...⛵\nBoat {boat2.name} is navigating...⛵\n')

def test_port_run() -> str:
    test = TestLoader().loadTestsFromTestCase(TestPort)
    with patch('sys.stdout', new_callable = StringIO) as fake_out:
        TextTestRunner(stream=fake_out, verbosity=2).run(test)
        result = fake_out.getvalue()
        return result

if __name__ == '__main__':
    print(test_port_run())