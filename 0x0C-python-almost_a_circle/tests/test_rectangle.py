#!/usr/bin/python3
"""defines tests for rectangle.py"""


import sys
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """class to test rectangle.py"""
    def test_args(self):
        self.assertEqual(Rectangle(10,2), 1)
