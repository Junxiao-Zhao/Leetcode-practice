# https://leetcode.com/problems/next-greater-element-ii/


def nextGreaterElements(nums: list[int]) -> list[int]:
    stack = nums[::-1][1:]
    result = [0] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop(-1)
        result[i] = -1 if not stack else stack[-1]
        stack.append(nums[i])

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    print(nextGreaterElements(nums))
