'''
Given a string s return the lenght of the longest sub string within that string
that has no repeated characters
'''

# Plan:
# naive approach: nested loop
# for each character, loop through the rest of the string until theres a repeated char
# whatever was the longest is the answer

def lengthOfLongestSubstring(self, s: str) -> int:
    maxlen = 0
    #Loop through each character
    for i, _ in enumerate(s):
        # initialize current character set
        current_sub = set()
        # loop through the rest of the characters
        for c2 in s[i:]:
            # check that the character isn't in the substring
            if c2 in current_sub:
                break
            else:
                # add it if it isn't
                current_sub.add(c2)
            # check to see if its longer than the current max
            if len(current_sub) > maxlen:
                maxlen = len(current_sub)
    return maxlen

# this will run in O(n^2) time in worst case.

# can I use a set to check the maximum possible length first?
# plan 2:
# cast string as set
# get length of set
# create a 'window' that length and see if it matches over a set
# if it does return that number, if not subrtract one and try window again

def lengthOfLongestSubstring(s: str) -> int:
    #get length of string as set
    maxlen = len(set(s))
    # the minimum return value will always be zero (empty string)
    while maxlen > 0:
        # move a window over the string
        for i in range(len(s)-maxlen+1):
            # if the window has no repeated chars its the max length
            if len(set(s[i:i+maxlen])) == maxlen:
                return maxlen
        # if the window got to the end and didn't find one get smaller and try again
        maxlen -=1
    return maxlen

# this is certainly a prettier solution, but I don't actually know that its faster
# the while loop will run a maximum of maxlen times (so larger number of chars means longer runtime)
# the for loop runs len(s)-maxlen times each time, and maxlen gets smaller each time
# worst case I think this is still O(n^2), possibly O(n log n)
# average case though I think is O(log n)
