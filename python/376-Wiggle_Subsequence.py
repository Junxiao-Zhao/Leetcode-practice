# https://leetcode.com/problems/wiggle-subsequence/


def wiggleMaxLength(nums: list):
    n = len(nums)
    if n < 2:
        return n

    prevdiff = nums[1] - nums[0]
    ret = (2 if prevdiff != 0 else 1)
    for i in range(2, n):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
            ret += 1
            prevdiff = diff

    return ret


if __name__ == "__main__":
    nums = [1, 1, 7, 4, 9, 2, 5]
    print(wiggleMaxLength(nums))
