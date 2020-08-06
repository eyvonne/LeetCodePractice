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
# I believe that this code runs in O(n log n) time.


def find_substring(word):
    # helper function to check if a given palendrome is part of a larger palendrome
    def extend_pal(word, index, factor):
        # normalize ref because Aba is a palendrome
        ref = word.lower()
        # create the palendrome
        pal = word[index:index + factor]
        # set the start and end of the palendrome check
        if index - 1 >= 0 and index + factor < len(word):
            a = index - 1
            b = index + factor
        else:
            return pal
        # move out the edges of the palendrome until they don't match
        while ref[a] == ref[b]:
            pal = word[a:b+1]
            # check that we haven't reached the end of the string
            if a - 1 >= 0 and b + 1 < len(word):
                a -= 1
                b += 1
            else:
                # thats as good as it gets if either end has been reached
                break
        return pal
    # if the word is a palendrome then it's always the longest palendrome
    if word == word[::-1]:
        return word
    # otherwise, pal should be the first letter to start
    pal = word[0] if len(word) > 0 else ''
    for i, _ in enumerate(word):
        # check that i isn't too large and is at a two letter palendrome
        if i+2 <= len(word) and word[i] == word[i+1]:
            # extend_pal just finds how big the pal is
            extension = extend_pal(word, i, 2)
            # if its longer than the longest save it
            if len(extension) > len(pal):
                pal = extension
        # essentially the same as other block
        if i+3 <= len(word) and word[i] == word[i+2]:
            extension = extend_pal(word, i, 3)
            if len(extension) > len(pal):
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
