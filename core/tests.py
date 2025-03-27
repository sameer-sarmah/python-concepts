from operations.add import add
from operations.mul import mul as multiply
import unittest

class TestOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2), 3)
    def test_mul(self):
        self.assertEqual(multiply(2,2), 4)