'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''


# Plan:
# the zigzag pattern is the same as doing a row that is vertical - head and tail
# convert string to list
# pop off n elements into first column
# pop off n-2 elements for the second
# repeat until all are off
# transpose the lists and read off (will run in n^2 time)

# Alternate:
# first element of solution is s[0]
# second element is s[n]
# third is s[2n] unless thats the end
# next row starts at s[1]
# followed by s[n + 1]
# followed by s[2n + 1]
# outer for loop is for i in range(n)
# inner for loop is while xn < len(s) where x is the current itteration

# alternate alternate:
# pull off first 'row'
# count used indexes in set
# loop while used set is smaller than s
# Track last row
# itterate through last row and pull off n-1 and n+1 if not in used

def convert(s, numRows):
    output = ''
    used = set()
    last_row = []
    x = 0
    # establish first row
    while x * (2 * numRows - 2) < len(s) and x*(2*numRows-2) not in used:
        output += s[x*(2*numRows-2)]
        used.add(x*(numRows*2-2))
        last_row.append(x*(2*numRows-2))
        x += 1
    # get the other rows, one at a time
    while len(used) < len(s):
        next_row = []
        for x in last_row:
            if x-1 > 0 and x-1 not in used:
                output += s[x-1]
                used.add(x-1)
                next_row.append(x-1)
            if x+1 < len(s) and x+1 not in used:
                output += s[x+1]
                used.add(x+1)
                next_row.append(x+1)
        last_row = next_row.copy()
    return output
