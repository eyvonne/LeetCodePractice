''' test module for palindromic substring'''

import unittest
import timeout_decorator
from palendromic_substring import find_substring


class TestPalendomicSubstring(unittest.TestCase):
    def test_base_case(self):
        word = 'abbaccdda'
        response = 'abba'
        self.assertEqual(find_substring(word), response)

    def test_no_palindrome(self):
        word = 'abcdefg'
        response = ''
        self.assertIn(find_substring(word), response)

    def test_short_pal(self):
        word = 'abacddaddc'
        response = 'cddaddc'
        self.assertEqual(find_substring(word), response)
        word = 'ababbabacd'
        response = 'ababbaba'
        self.assertEqual(find_substring(word), response)

    def test_pal_in_pal(self):
        word = 'ffwcbadabcdde'
        response = 'cbadabc'
        self.assertEqual(find_substring(word), response)

    @timeout_decorator.timeout(200)
    def test_long_string(self):
        word = 'asdlklkboiwasdlkjvbiaowelkjadscbaijebuilakmniuewlbjakwecuilbonajkldshafjlciewsablkwebsuicbniusaebacuiwejbkgfmdceauwibklsdfhaisdufnkjbaueiysblvjsdnclakjwefdfbjndlciueaweuibvzsjbnxcmnobaliuesglincsdwnavjsdnpqWMNVRAWUBCDSnaoisdmvivpsdfmcaeslizubajsdlabcuioasdkjnvueaskjbviuesablkjsdncacmalsdjnaifsdbfiuoebsfwljwanergti;odslkanfajsdhbcyufavhpasgfjlaksdmicubalsedjkbegaosidjvsklasdfnqiejBUUIWVNIFABklasdjklfnwoeioqwertyuiopasdfghjklzxcvbnmmmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmmnbvcxzasdlklkboiwasdlkjvbiaowelkjadscbaijebuilakmniuewlbjakwecuilbonajkldshafjlciewsablkwebsuicbniusaebacuiwejbkgfmdceauwibklsdfhaisdufnkjbaueiysblvjsdnclakjwefdfbjndlciueaweuibvzsjbnxcmnobaliuesglincsdwnavjsdnpqWMNVRAWUBCDSnaoisdmvivpsdfmcaeslizubajsdlabcuioasdkjnvueaskjbviuesablkjsdncacmalsdjnaifsdbfiuoebsfwljwanergti;odslkanfajsdhbcyufavhpasgfjlaksdmicubalsedjkbegaosidjvsklasdfnqiejBUUIWVNIFABklasdjklfnwoeioqwertyuiopasdfghjkl'
        response = 'zxcvbnmmnbvcxz'
        self.assertEqual(find_substring(word), response)

    def test_capitals(self):
        word = 'Abbacdc'
        response = 'Abba'
        self.assertEqual(find_substring(word), response)
        word = 'AABBAAcdfae'
        response = 'AABBAA'
        self.assertEqual(find_substring(word), response)

    def test_non_alpha(self):
        word = '1221341'
        response = '1221'
        self.assertEqual(find_substring(word), response)
        word = ';fdsksdf;ewc;2'
        response = ';fdsksdf;'
        self.assertEqual(find_substring(word), response)

    def test_short_string(self):
        word = 'aa'
        self.assertEqual(find_substring(word), 'aa')

    def test_empty_string(self):
        word = ''
        self.assertEqual(find_substring(word), '')


if __name__ == '__main__':
    unittest.main()
