import unittest
import pytest

from factorials import rec_fact 

class FactorialTest(unittest.TestCase):

    def test_rec_fact(self):
        self.assertEqual(rec_fact(4), 24)