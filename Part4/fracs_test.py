from fracs import *
import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 4], [2, 4]), [1, 1])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([1, 4], [1, 8]), [1, 8])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([1, 3], [3, 7]), [1, 7])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([8, 3], [7, 2]), [16, 21])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([1, 2]), False)
        self.assertEqual(is_zero([0, 2]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([-1, 5], [1, 5]), -1)
        self.assertEqual(cmp_frac([1, 5], [1, 5]), 0)
        self.assertEqual(cmp_frac([1, 5], [-1, 5]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, 4]), 0.25)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
