# https://leetcode.com/problems/non-decreasing-array/


def checkPossibility(nums: list):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if i == 0:
                nums[i] = nums[i + 1]
                count += 1
            elif nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i + 1]
                count += 1
            else:
                nums[i + 1] = nums[i]
                count += 1

    return count < 2
