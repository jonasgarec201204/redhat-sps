import unittest
import cv10 as RS
rs1 = RS.ReverseString("ahoj jak se mas")
class TestReverseString(unittest.TestCase):
    def test1(self):
        self.assertEqual(rs1.reverse(), "sam es kaj joha")
    def test2(self):
        self.assertNotEqual(rs1.reverse(), "ahoj jak se mas")
if __name__ == "__main__":
    unittest.main()
