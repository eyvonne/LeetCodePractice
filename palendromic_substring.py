'''Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"'''

# Plan:
# iterate through the two letter and three letter combos in the string
# if the two or three is a palendrome check one letter out for also being a palendrome


def find_substring(word):
    # helper to check that any given string is a palendrome
    def is_pal(subword: str) -> bool:
        return subword == subword[::-1]
    # helper function to check if a given palendrome is part of a larger palendrome

    def extend_pal(word, index, factor):
        ref = word.lower()
        a = index-1
        b = index+factor
        pal = word[index:index+factor]
        while ref[a] == ref[b]:
            pal = word[a:b+1]
            if a - 1 >= 0 and b + 1 < len(word):
                a -= 1
                b += 1
            else:
                break
        return pal
    # if the word is a palendrome then it's always the longest palendrome
    if is_pal(word):
        return word

    pal = ''
    max = 0
    for i in range(len(word)-2):
        if is_pal(word[i:i+2]):
            extension = extend_pal(word, i, 2)
            if len(extension) > max:
                max = len(extension)
                pal = extension
        if i+3 < len(word) and is_pal(word[i:i+3]):
            extension = extend_pal(word, i, 3)
            if len(extension) > max:
                max = len(extension)
                pal = extension
    return pal


def find_substring_slow(word):
    def is_pal(subWord: str) -> bool:
        return subWord == subWord[::-1]

    pal = ''
    max = 0
    for i, letter in enumerate(word):
        if letter.lower() in set(word[i+1:].lower()):
            for q, _ in enumerate(word[i:], i+1):
                sub = word[i:q].lower()
                if is_pal(sub):
                    if len(sub) > max:
                        pal = word[i:q]
                        max = len(sub)
    return pal
