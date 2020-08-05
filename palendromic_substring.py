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
