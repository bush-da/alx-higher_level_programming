#!/usr/bin/python3
""" Defines a unittest for rectangle class """


import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle_instantiation(unittest.TestCase):

    def test_with_int_args(self):
        result = Rectangle(2, 3)
        result1 = Rectangle(1, 3)
        self.assertEqual(result.id, result1.id - 1)
        self.assertEqual(result1.id, result.id + 1)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_three_args(self):
        result = Rectangle(1, 2, 3)
        result1 = Rectangle(1, 3, 4)
        self.assertEqual(result.id, result1.id - 1)

    def test_with_four_args(self):
        result = Rectangle(1, 2, 3, 4)
        result1 = Rectangle(5, 6, 7, 8)
        self.assertEqual(result.id, result1.id - 1)

    def test_with_five_args(self):
        result = Rectangle(1, 2, 3, 4, 5)
        result1 = Rectangle(5, 6, 7, 7, 8)
        self.assertEqual(result.id, 5)

    def test_non_integer_args(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_instance_of_base(self):
        self.assertIsInstance(Rectangle(1, 9), Base)


if __name__ == "__main__":
    unittest.main()
