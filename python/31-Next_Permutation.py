# https://leetcode.com/problems/next-permutation/


def nextPermutation(nums: list):
    i = j = len(nums) - 1

    while i > 0:
        if nums[i - 1] < nums[i]:
            break
        i -= 1

    if i != 0:
        while j >= i and nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

    j = len(nums) - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
