#!/usr/bin/python3
""" Add Unitests """


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ max_integer Unittest """

    def test_positive(self):
        """ Tests for all positive """
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def test_begginning(self):
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_positive_middle(self):
        """ Tests for all positive in a list """
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def test_negative(self):
        """ Tests list for negative number """
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_list(self):
        """ Tests for empty list """
        e = []
        self.assertIsNone(max_integer(e))

    def test_element(self):
        """ Tests for one number """
        o = [1]
        self.assertEqual(max_integer(o), 1)
