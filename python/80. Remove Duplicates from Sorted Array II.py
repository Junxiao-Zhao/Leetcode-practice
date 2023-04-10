# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

from collections import defaultdict


def removeDuplicates(self, nums: list[int]) -> int:
    count = defaultdict(int)
    j = 0

    for i, n in enumerate(nums):
        count[n] += 1
        if count[n] <= 2:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return j
