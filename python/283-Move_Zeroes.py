# https://leetcode.com/problems/move-zeroes/


def moveZeroes(nums: list):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
