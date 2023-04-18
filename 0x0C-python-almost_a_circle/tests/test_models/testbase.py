#!/usr/bin/python3
""" defines unittest for base.py"""

import unittest
from models.base import Base


class TestBase_init(unittest.TestCase):
    """ unitest for base class instantiation"""


    def test_with_no_args(self):
        result = Base()
        result1 = Base()
        self.assertEqual(result.id, result1.id - 1)

    def test_with_args(self):
        result = Base(10)
        self.assertEqual(result.id, 10)
        result = Base(-1)
        self.assertEqual(result.id, -1)

    def test_with_None_id(self):
        result = Base(None)
        result1 = Base(None)
        self.assertEqual(result.id, result1.id - 1)

    def test_id_with_public(self):
        result = Base(10)
        result.id = 20
        self.assertEqual(result.id, 20)


if __name__ == "__main__":
    unittest.main()
