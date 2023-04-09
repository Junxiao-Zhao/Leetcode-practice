# https://leetcode.com/problems/find-peak-element/


def findPeakElement(nums: list):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if (nums[mid] > nums[mid - 1] if mid > 0 else True) and (
                nums[mid] > nums[mid + 1] if mid + 1 < len(nums) else True):
            return mid
        elif (nums[mid] < nums[mid - 1] if mid > 0 else False):
            r = mid - 1
        else:
            l = mid + 1

    return (l + r) // 2
