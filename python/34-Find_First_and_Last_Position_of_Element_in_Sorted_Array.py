# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


def binary(nums, l, r, target):
    while l <= r:
        mid = (r + l) // 2

        if nums[mid] == target:
            start, _ = binary(nums, l, mid - 1, target)
            _, end = binary(nums, mid + 1, r, target)

            if start == -1:
                start = mid
            if end == -1:
                end = mid
            return [start, end]

        elif nums[mid] > target:
            r = mid - 1

        else:
            l = mid + 1

    return [-1, -1]


def searchRange(nums: list, target: int):
    return binary(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    print(searchRange(nums, 6))
