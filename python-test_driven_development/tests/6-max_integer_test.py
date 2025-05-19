#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define un caso de prueba para la función max_integer.
    """

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

    def test_duplicate_integers(self):
        self.assertEqual(max_integer([1, 2, 2, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 2000000, 3000000]), 3000000)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)

    def test_mixed_ints_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
