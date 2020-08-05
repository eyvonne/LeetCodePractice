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

    pals = {}
    for i, _ in enumerate(word):
        for q, _ in enumerate(word[i:], i):
            sub = word[i:q+1].lower()
            if len(sub) > 0:
                if is_pal(sub):
                    if len(sub) in pals:
                        pals[len(sub)].append(sub)
                    else:
                        pals[len(sub)] = [sub]
    try:
        return pals[max(pals)][0]
    except:
        return None
