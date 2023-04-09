# https://leetcode.com/problems/permutations/


def backtracking(nums: list, ans: list, level: int):
    if level == len(nums) - 1:
        ans.append(nums.copy())
        return

    for i in range(level, len(nums)):
        nums[i], nums[level] = nums[level], nums[i]
        backtracking(nums, ans, level + 1)
        nums[i], nums[level] = nums[level], nums[i]


def permute(nums: list):
    ans = []
    backtracking(nums, ans, 0)
    return ans


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))
