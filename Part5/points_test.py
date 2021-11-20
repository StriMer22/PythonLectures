import unittest
from points import Point

# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_print(self):
        self.assertEqual("Point(1, 1)", repr(Point(1, 1)))
        self.assertEqual("Point(0, 0)", repr(Point(0, 0)))
        self.assertEqual("Point(-6, -6)", repr(Point(-6, -6)))
        self.assertEqual("Point(10, -2)", repr(Point(10, -2)))
        self.assertEqual("(-6, -6)", str(Point(-6, -6)))
        self.assertEqual("(0, 0)", str(Point(0, 0)))
        self.assertEqual("(0, 2)", str(Point(0, 2)))
        self.assertEqual("(2, -2)", str(Point(2, -2)))

    def test_cmp(self):
        self.assertTrue(Point(1, 0) == Point(1, 0))
        self.assertTrue(Point(1, 3) != Point(1, 2))
        self.assertTrue(Point(-1, 20) == Point(-1, 20))
        self.assertTrue(Point(-9, 11) != Point(11, 9))

    def test_add(self):
        self.assertEqual(Point(1, 0), Point(0, -1) + Point(1, 1))
        self.assertEqual(Point(1, 3), Point(1, -5) + Point(0, 8))
        self.assertEqual(Point(1, 11), Point(-20, 1) + Point(21, 10))
        self.assertEqual(Point(-1, -1), Point(0, 0) + Point(-1, -1))

    def test_sub(self):
        self.assertEqual(Point(-1, -2), Point(0, -1) - Point(1, 1))
        self.assertEqual(Point(0, -8), Point(0, 0) - Point(0, 8))
        self.assertEqual(Point(1, 0), Point(2, 5) - Point(1, 5))
        self.assertEqual(Point(-21, -9), Point(-30, 1) - Point(-9, 10))

    def test_mul(self):
        self.assertEqual(-10, Point(0, -1) * Point(1, 10))
        self.assertEqual(-25, Point(1, -5) * Point(0, 5))
        self.assertEqual(29, Point(2, 3) * Point(1, 9))
        self.assertEqual(1, Point(-3, 1) * Point(3, 10))

    def test_cross(self):
        self.assertEqual(1, Point(0, -1).cross(Point(1, 1)))
        self.assertEqual(-2, Point(2, 4).cross(Point(2, 3)))
        self.assertEqual(16, Point(10, 2).cross(Point(2, 2)))
        self.assertEqual(0, Point(-1, -1).cross(Point(1, 1)))

    def test_length(self):
        self.assertEqual(1, Point(0, -1).length())
        self.assertEqual(5, Point(3, 4).length())
        self.assertEqual(10, Point(6, 8).length())

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
