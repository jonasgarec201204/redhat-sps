import unittest
import cv4 as fact
class TestFactorial(unittest.TestCase):
    def test1(self):
        self.assertEqual(fact.factorial(10), 3628800)
    def test2(self):
        self.assertEqual(fact.factorial(5), 120)
if __name__ == "__main__":
    unittest.main()
