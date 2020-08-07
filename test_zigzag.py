import unittest
from zigzag import convert


class TestZigZag(unittest.TestCase):
    def test_example1(self):
        input = "PAYPALISHIRING"
        output = 'PAHNAPLSIIGYIR'
        self.assertEqual(convert(input, 3), output)

    def test_example2(self):
        input = 'PAYPALISHIRING'
        output = 'PINALSIGYAHRPI'
        self.assertEqual(convert(input, 4), output)

    def test_capitals(self):
        input = 'ABCdefG'
        output = 'AeBdfCG'
        self.assertEqual(convert(input, 3), output)

    def test_spaces(self):
        input = 'ab cdef'
        output = 'adbce f'
        self.assertEqual(convert(input, 3), output)

    def test_large_n(self):
        input = 'abcde'
        self.assertEqual(convert(input, 6), input)
        input = 'abcdefabcdefabcdefabcdef'
        output = 'acbbdcaedffeefdacbbcadfe'
        self.assertEqual(convert(input, 11), output)

    def test_small_n(self):
        input = 'abcdef'
        output = 'acebdf'
        self.assertEqual(convert(input, 2), output)
        self.assertEqual(convert(input, 1), input)
        input = 'abcd'
        output = 'abdc'
        self.assertEqual(convert(input, 3), output)


if __name__ == '__main__':
    unittest.main()
