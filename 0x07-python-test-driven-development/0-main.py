#!/usr/bin/python3

import unittest
add_integer = __import__("0-add_integer").add_integer


class TestAddInteger(unittest.TestCase):
    def test_add_integer(self):
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(1.2, 4.5), 5)
        self.assertEqual(add_integer(2), 100)
        self.assertEqual(add_integer(-2, -14), -16)

        with self.assertRaises(TypeError):
            add_integer('1', 3)
        with self.assertRaises(TypeError):
            add_integer(1, '2')
        with self.assertRaises(TypeError):
            add_integer("1", "2")


if __name__ == "__main__":
    unittest.main()
