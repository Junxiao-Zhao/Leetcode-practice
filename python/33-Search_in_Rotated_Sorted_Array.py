# https://leetcode.com/problems/search-in-rotated-sorted-array/


def search(nums: list, target: int):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif target >= nums[l] and target < nums[mid]:
            r = mid - 1
        elif target > nums[mid] and target <= nums[r]:
            l = mid + 1
        elif target > nums[mid]:
            r -= 1
        else:
            l += 1

    return -1
