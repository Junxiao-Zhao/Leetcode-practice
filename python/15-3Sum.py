# https://leetcode.com/problems/3sum/


def threeSum(nums: list):
    nums.sort()
    ans = []
    prev_k = len(nums)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        k = prev_k - 1
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            while k > j and nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            if j == k:
                break
            if nums[i] + nums[j] + nums[k] == 0:
                ans.append([nums[i], nums[j], nums[k]])

    return ans


if __name__ == "__main__":
    nums = [0, 0, 0, 0]
    print(threeSum(nums))
