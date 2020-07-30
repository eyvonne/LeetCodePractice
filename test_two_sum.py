import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):

    def test_base_case(self):
        l = [2, 3, 5, 7]
        result = two_sum(l, 8)
        self.assertEqual(result, (1, 2))
        result2 = two_sum(l, 5)
        self.assertEqual(result2, (0, 1))
        result3 = two_sum(l, 12)
        self.assertEqual(result3, (2, 3))
        result4 = two_sum(l, 7)
        self.assertEqual(result4, (0, 2))
        result5 = two_sum(l, 9)
        self.assertEqual(result5, (0, 3))
        # this test also ensures that it won't return (2, 2)
        # which is an edge case that wasn't included
        self.assertEqual(two_sum(l, 10), (1, 3))

    def test_add_zero(self):
        l = [2, 3, 0, 5]
        result = two_sum(l, 3)
        self.assertEqual(result, (1, 2))
        self.assertEqual(two_sum(l, 2), (0, 2))
        self.assertEqual(two_sum(l, 5), (2, 3))

    def test_add_neg(self):
        # test that a single negative number won't break it
        l = [-1, 2, 4, 5]
        self.assertEqual(two_sum(l, 1), (0, 1))
        self.assertEqual(two_sum(l, 3), (0, 2))
        self.assertEqual(two_sum(l, 4), (0, 3))
        # test that a negative target won't break it
        l2 = [-5, 1, 3, 4, 5]
        self.assertEqual(two_sum(l2, -4), (0, 1))
        self.assertEqual(two_sum(l2, -2), (0, 2))
        self.assertEqual(two_sum(l2, -1), (0, 3))
        self.assertEqual(two_sum(l2, 0), (0, 4))

    def test_dual_neg(self):
        # test that it can add two negative numbers
        l = [-2, -3, -4, -10]
        self.assertEqual(two_sum(l, -5), (0, 1))
        self.assertEqual(two_sum(l, -6), (0, 2))
        self.assertEqual(two_sum(l, -12), (0, 3))
        self.assertEqual(two_sum(l, -7), (1, 2))
        self.assertEqual(two_sum(l, -13), (1, 3))
        self.assertEqual(two_sum(l, -14), (2, 3))

    def test_errors(self):
        l = []


if __name__ == '__main__':
    unittest.main()
