# https://leetcode.com/problems/move-zeroes/


def moveZeroes(nums: list):
    i, j = 0, 1
    while i < len(nums) and j < len(nums):
        if nums[i] != 0:
            i += 1
            j = i + 1
        elif nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[j] == 0:
            j += 1
