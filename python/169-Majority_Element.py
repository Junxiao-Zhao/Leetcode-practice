# https://leetcode.com/problems/majority-element/


def majorityElement(nums: list):
    count = dict()

    for each in nums:
        count.setdefault(each, 0)
        count[each] += 1
        if count[each] > len(nums) // 2:
            return each
