# https://leetcode.com/problems/max-consecutive-ones-iii/


def longestOnes(nums: list, k: int):
    l = r = 0
    max_len = cur_len = 0
    count = dict()
    count[0] = 0
    count[1] = 0

    while r < len(nums):
        count[nums[r]] += 1
        cur_len += 1
        if count[0] <= k:
            max_len = max(max_len, cur_len)
        else:
            count[nums[l]] -= 1
            l += 1
            cur_len -= 1

        r += 1

    return max_len
