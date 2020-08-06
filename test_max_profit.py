import unittest
from max_profit import max_profit
import numpy as np
import timeout_decorator


class TestMaxProfit(unittest.TestCase):
    def test_base_case(self):
        stocks = [1, 2, 4, 6, 7]
        response = 6
        self.assertEqual(max_profit(stocks), response)

    def test_neg_numbers(self):
        stocks = [-7, 3, 5, 2, 9]
        response = 16
        self.assertEqual(max_profit(stocks), response)
        stocks = [-7, -8, -5, -4, -2, -9]
        response = 6
        self.assertEqual(max_profit(stocks), response)

    def test_end(self):
        stocks = [9, 6, 7, 8, 1, 5]
        response = 4
        self.assertEqual(max_profit(stocks), response)

    def test_beginning(self):
        stocks = [1, 9, 2, 4, 6, 3]
        response = 8
        self.assertEqual(max_profit(stocks), response)

    def test_repeats(self):
        stocks = [2, 2, 2, 4, 5, 8, 2]
        response = 6
        self.assertEqual(max_profit(stocks), response)
        stocks = [2, 3, 4, 5, 6, 7, 7, 7, 7]
        response = 5
        self.assertEqual(max_profit(stocks), response)

    def test_no_answer(self):
        stocks = [7, 6, 5, 4, 3, 2, 1]
        response = 0
        self.assertEqual(max_profit(stocks), response)
        stocks = [7, 7, 7, 7, 7, 7]
        self.assertEqual(max_profit(stocks), response)

    def test_multiple_answer(self):
        stocks = [1, 7, 1, 7, 1, 7]
        response = 6
        self.assertEqual(max_profit(stocks), response)

    def test_empty_list(self):
        stocks = []
        response = 0
        self.assertEqual(max_profit(stocks), response)

    def test_buy_first(self):
        stocks = [9, 1, 3, 5, 7]
        response = 6
        self.assertEqual(max_profit(stocks), response)

    @timeout_decorator.timeout(200)
    def test_huge_array(self):
        stocks = [1] + list(np.random.randint(2, 1000, 1000)) + [1005]
        response = 1004
        self.assertEqual(max_profit(stocks), response)


if __name__ == '__main__':
    unittest.main()
