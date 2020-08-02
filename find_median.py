from typing import List
''' given two sorted arrays find the median of both'''

# the ideal solution will run in O(log(m+n))
# this solution runs in O(m+n) time
# I might have to come back to this, I'm feeling tired now

# https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
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
def findMedianSortedArrays2(nums1: List[int], nums2: List[int]):
    if len(nums1) == 0 or len(nums2) == 0:
        if len(nums1) == 0:
            if len(nums2) % 2
    total_len = len(nums1) + len(nums2)
    median = None
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

if __name__ == '__main__':
    arr1 = [1,3]
    arr2 = [2,4]

    print(findMedianSortedArrays2(arr1, arr2))
