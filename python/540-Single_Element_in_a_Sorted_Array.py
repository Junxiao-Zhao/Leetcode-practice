# https://leetcode.com/problems/single-element-in-a-sorted-array/


def singleNonDuplicate(nums: list):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if mid % 2:
            if mid != l and nums[mid] == nums[mid - 1]:
                l = mid + 1
            elif mid != r and nums[mid] == nums[mid + 1]:
                r = mid - 1
            else:
                return nums[mid]
        else:
            if mid != r and nums[mid] == nums[mid + 1]:
                l = mid + 2
            elif mid != l and nums[mid] == nums[mid - 1]:
                r = mid - 2
            else:
                return nums[mid]

    return nums[r]


if __name__ == "__main__":
    nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(singleNonDuplicate(nums))
