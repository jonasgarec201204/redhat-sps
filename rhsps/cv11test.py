import unittest
import cv11 as areaT
triangle1 = areaT.TriangleArea(2, 2, 90)
class TestArea(unittest.TestCase):
    def test1(self):
        self.assertEqual(triangle1.area(), 2)
if __name__ == "__main__":
    unittest.main()
