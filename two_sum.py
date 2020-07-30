'''given an array of integers retun indicies of the two numbers such that they
add up to a specific target

You may assume that each input would have exactly one solution and you may not
use the same element twice
'''

# Planning phase:
# this looks like a hash table problem when optimized
# create two pointers
# iterate through the list, incrementing one pointer
# if it gets all the way to the end reset it to the first pointer
# and advance both by one.
# This solution runs in O(n log n) time
# one of the tests that I didn't write was for time, and I need to improve


def two_sum(nums, target):
    i, q = 0, 1
    searching = True
    while searching:
        # if found the right pair
        if nums[i] + nums[q] == target:
            searching = False
        else:
            # check that q can move up
            if q < len(nums) - 1:
                q += 1
            # if it can't, advance i and move q
            else:
                i += 1
                q = i + 1
    return i, q
