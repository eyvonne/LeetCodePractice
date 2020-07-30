import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):

    def test_base_case(self):
        result = two_sum([2, 3, 5, 7], 8)
        self.assertEqual(result, (1, 2))

    def test_has_answer(self):
        result = two_sum([2, 3, 5, 7], 8)
        self.assert


if __name__ == '__main__':
    unittest.main()
