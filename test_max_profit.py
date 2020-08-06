import unittest
from max_profit import max_profit


class TestMaxProfit(unittest.TestCase):
    def test_base_case(self):
        stocks = [1, 2, 4, 6, 7]
        response = 4
        self.assertEqual(max_profit(stocks), response)

    def test_neg_numbers(self):
        stocks = [-7, 3, 5, 2, 9]
        response = 4
        self.assertEqual(max_profit(stocks), response)
        stocks = [-7, -8, -5, -4, -2, -9]
        response = 4
        self.assertEqual(max_profit(stocks), response)

    def test_end(self):
        stocks = [9, 6, 7, 8, 1, 5]
        response = 5
        self.assertEqual(max_profit(stocks), response)

    def test_beginning(self):
        stocks = [1, 9, 2, 4, 6, 3]
        response = 1
        self.assertEqual(max_profit(stocks), response)

    def test_repeats(self):
        stocks = [2, 2, 2, 4, 5, 8, 2]
        response = 5
        self.assertEqual(max_profit(stocks), response)
        stocks = [2, 3, 4, 5, 6, 7, 7, 7, 7]
        response = [5, 6, 7, 8]
        self.assertIn(max_profit(stocks), response)

    def test_no_answer(self):
        stocks = [7, 6, 5, 4, 3, 2, 1]
        response = 0
        self.assertEqual(max_profit(stocks), response)
        stocks = [7, 7, 7, 7, 7, 7]
        self.assertEqual(max_profit(stocks), response)
