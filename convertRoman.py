'''write code to translate a string in roman numerals to integers'''
# Plan:
# create a dict of roman numerals
# iterate through the given string,
# if the next char is greater than the current char
# add current char as negative value
# else
# add current char as positive value
import sys

romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_arabic(roman):
    arabic = 0
    for i in range(len(roman) - 1):  # skip the last char so the if works
        if romans[roman[i]] < romans[roman[i + 1]]:
            arabic -= romans[roman[i]]
        else:
            arabic += romans[roman[i]]
    arabic += romans[roman[-1]]  # the final character will always be added
    return arabic


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(roman_to_arabic(sys.argv[1]))
    else:
        print(roman_to_arabic('CLVII'))
