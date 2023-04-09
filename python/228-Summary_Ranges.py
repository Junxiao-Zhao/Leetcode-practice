# https://leetcode.com/problems/summary-ranges/


def summaryRanges(nums: list):
    if len(nums) == 0:
        return []

    ans = [str(nums[0])]

    for i in range(1, len(nums) + 1):
        if i == len(nums) or nums[i - 1] != nums[i] - 1:
            if int(ans[-1]) != nums[i - 1]:
                ans[-1] += "->" + str(nums[i - 1])
            if i < len(nums):
                ans.append(str(nums[i]))

    return ans
