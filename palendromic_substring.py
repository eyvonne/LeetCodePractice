'''Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"'''


def find_substring(word):
    def is_pal(subWord:str) -> bool:
        return subWord == subWord[::-1]

    pals = []
    for i, _ in enumerate(word):
        for q, _ in enumerate(word[i+1:]):
            if is_pal(word[i:q+1]):
                pals.append(word[i:q+1])
    max = 0
    maxpal = None
    for pal in pals:
        if len(pal) > max:
            max = len(pal)
            maxpal = pal

    return pal
