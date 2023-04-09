# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/


def longestSubarray(nums: list, limit: int):
    from sortedcontainers import SortedList
    l = r = 0
    cur_len = max_len = 0
    window = SortedList()

    while r < len(nums):
        cur_len += 1
        window.add(nums[r])

        if window[-1] - window[0] > limit:
            window.remove(nums[l])
            l += 1
            cur_len -= 1
        else:
            max_len = max(max_len, cur_len)

        r += 1
    return max_len


if __name__ == "__main__":
    nums = [8, 2, 4, 7]
    print(longestSubarray(nums, 4))
