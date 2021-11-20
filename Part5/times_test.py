import unittest
from times import Time
# Kod testujący moduł.


class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):      # test str() i repr()
        self.assertEqual("Time(1)", repr(Time(1)))
        self.assertEqual("Time(11)", repr(Time(11)))
        self.assertEqual("Time(5)", repr(Time(5)))
        self.assertEqual("01:05:13", str(Time(3913)))
        self.assertEqual("00:33:07", str(Time(1987)))
        self.assertEqual("00:00:52", str(Time(52)))

    def test_cmp(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertFalse(Time(1) == Time(2))
        self.assertTrue(Time(1) != Time(2))
        self.assertFalse(Time(1) != Time(1))
        self.assertTrue(Time(1) < Time(2))
        self.assertFalse(Time(2) < Time(1))
        self.assertTrue(Time(1) <= Time(2))
        self.assertFalse(Time(2) <= Time(1))
        self.assertTrue(Time(2) > Time(1))
        self.assertFalse(Time(1) > Time(2))
        self.assertTrue(Time(2) >= Time(1))
        self.assertFalse(Time(1) >= Time(2))

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(3), Time(1) + Time(2))
        self.assertEqual(Time(1), Time(1) + Time(0))
        self.assertEqual(Time(0), Time(0) + Time(0))
        self.assertEqual(Time(-7), Time(-9) + Time(2))
        self.assertEqual(Time(0), Time(-12) + Time(12))

    def test_int(self):
        self.assertEqual(int(Time(1)), 1)
        self.assertEqual(int(Time(-8)), -8)
        self.assertEqual(int(Time(0)), 0)
        self.assertEqual(int(Time(1111)), 1111)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()     # wszystkie testy
