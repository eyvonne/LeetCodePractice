from typing import List
from random import sample
from time import time
''' given two sorted arrays find the median of both'''

# the ideal solution will run in O(log(m+n))
# this solution runs in O(m+n) time
# I might have to come back to this, I'm feeling tired now

# https://leetcode.com/problems/median-of-two-sorted-arrays/


def findMedianSortedArraysSlow(nums1: List[int], nums2: List[int]) -> float:
    def helper(nums1, nums2, all_nums):
        if len(nums1) == 0:
            all_nums += nums2
            return all_nums
        if len(nums2) == 0:
            all_nums += nums1
            return all_nums

        i = nums1[0]
        j = nums2[0]
        if i < j:
            all_nums.append(i)
            if len(nums1) > 1:
                return helper(nums1[1:], nums2, all_nums)
            else:
                return helper([], nums2, all_nums)
        elif j < i:
            all_nums.append(j)
            if len(nums2) > 1:
                return helper(nums1, nums2[1:], all_nums)
            else:
                return helper(nums1, [], all_nums)

    nums = helper(nums1, nums2, [])
    if len(nums) % 2 == 0:
        return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
    else:
        return nums[len(nums)//2]

# this one runs in O(log n + m) time


class Solution():
    def __init__(self):
        pass

    def findMedianSortedArraysBroke(self, nums1: List[int], nums2: List[int]):
        total_len = len(nums1) + len(nums2)
        median = None
        if len(nums1) == 0:
            return findMedianSortedArrays(nums2[0:len(nums2)//2], nums2[len(nums2)//2:])
        if len(nums2) == 0:
            return findMedianSortedArrays(nums1[0:len(nums1)//2], nums1[len(nums1)//2:])
        if total_len % 2 == 0:
            for _ in range(total_len//2):
                if nums1[0] < nums2[0]:
                    med1 = nums1[0]
                    nums1 = nums1[1:]
                else:
                    med1 = nums2[0]
                    nums2 = nums2[1:]
            if nums1[0] < nums2[0]:
                med2 = nums1[0]
                nums1 = nums1[1:]
            else:
                med2 = nums2[0]
                nums2 = nums2[1:]
            median = (med1+med2) / 2
        else:
            for _ in range(total_len//2 + 1):
                breakpoint()
                if nums1[0] < nums2[0]:
                    median = nums1[0]
                    nums1 = nums1[1:]
                else:
                    median = nums2[0]
                    nums2 = nums2[1:]

        return median

# get total length
# create two pointers
# walk through the two lists
# when halfway, return the number


def findMedianSortedArrayshalf(nums1, nums2):
    total_len = len(nums1) + len(nums2)
    ptra = -1
    ptrb = -1
    median = None
    if total_len % 2 == 1:
        for i in range(total_len//2+1):
            breakpoint()
            if nums1[ptra + 1] < nums2[ptrb + 1]:
                ptra += 1 if len(nums1) - 2 > ptra else 0
                median = nums1[ptra]
            else:
                ptrb += 1 if len(nums2) - 2 > prtb else 0
                median = nums2[ptrb]
        return median


def findMedianSortedArraysSlow2(nums1: List[int], nums2: List[int]) -> float:
    total_len = len(nums1) + len(nums2)
    mid = total_len // 2

    def helper(nums1, nums2, all_nums):
        if len(nums1) == 0:
            all_nums += nums2
            return helper(nums2[0:len(nums2)//2], nums2[len(nums2)//2:])
        if len(nums2) == 0:
            all_nums += nums1
            return all_nums

        i = nums1[0]
        j = nums2[0]
        if i < j:
            all_nums.append(i)
            if len(nums1) > 1:
                return helper(nums1[1:], nums2, all_nums)
            else:
                return helper([], nums2, all_nums)
        elif j < i:
            all_nums.append(j)
            if len(nums2) > 1:
                return helper(nums1, nums2[1:], all_nums)
            else:
                return helper(nums1, [], all_nums)

    nums = helper(nums1, nums2, [])
    if len(nums) % 2 == 0:
        return (nums[len(nums)//2] + nums[len(nums)//2 - 1])/2
    else:
        return nums[len(nums)//2]

# lets try some massive recursion


def findMedianSortedArrays(nums1, nums2):
    count = 0
    total_len = len(nums1) + len(nums2)
    max = total_len // 2

    def findOddMedian(nums1, nums2, count, max):
        # make sure theres always something in both lists
        breakpoint()
        if len(nums1) == 0:
            if len(nums2) == 1:
                return nums2[0]
            else:
                return findOddMedian(nums2[0:len(nums2)//2], nums2[len(nums2)//2:], count, max)
        if len(nums2) == 0:
            if len(nums1) == 1:
                return nums1[0]
            else:
                return findOddMedian(nums1[0:len(nums1)//2], nums1[len(nums1)//2:], count, max)

        if count == max:
            # base case where we've found the median
            if nums1[0] < nums2[0]:
                return nums1[0]
            else:
                return nums2[0]
        else:
            count += 1
            if nums1[0] < nums2[0]:
                return findOddMedian(nums1[1:], nums2, count, max)
            else:
                return findOddMedian(nums1, nums2[1:], count, max)

    def findEvenMedian(nums1, nums2, count, max):
        if len(nums1) == 0:
            return findEvenMedian(nums2[0:len(nums2)//2], nums2[len(nums2)//2:], count, max)
        if len(nums2) == 0:
            return findEvenMedian(nums1[:len(nums1)//2], nums1[len(nums1)//2:], count, max)

        if count == max:
            if nums1[0] < nums2[0]:
                a = nums1[0]
                try:
                    if nums1[1] < nums2[0]:
                        b = nums1[1]
                    else:
                        b = nums2[0]
                except:
                    b = nums2[0]
            else:
                a = nums2[0]
                try:
                    if nums1[0] < nums2[1]:
                        b = nums1[0]
                    else:
                        b = nums2[1]
                except:
                    b = nums1[0]
            return (a+b)/2
        else:
            count += 1
            if nums1[0] < nums2[0]:
                return findEvenMedian(nums1[1:], nums2, count, max)
            else:
                return findEvenMedian(nums1, nums2[1:], count, max)

    if total_len % 2 == 0:
        max -= 1
        return findEvenMedian(nums1, nums2, count, max)
    else:
        return findOddMedian(nums1, nums2, count, max)


if __name__ == '__main__':
    arr1 = sample(range(10000000000000), 100000)
    arr2 = sample(range(10000000000000), 100000)
    arr1.sort()
    arr2.sort()
    print('starting benchmark')
    start = time()
    findMedianSortedArraysSlow(arr1, arr2)
    mid = time()
    findMedianSortedArrays(arr1, arr2)
    end = time()

    print(f'original {mid-start}, logtime {end-mid}')
