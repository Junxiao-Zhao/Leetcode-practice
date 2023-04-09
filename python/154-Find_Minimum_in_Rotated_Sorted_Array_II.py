# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/


def findMin(nums: list):

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if mid != 0 and nums[mid - 1] > nums[mid]:
            return nums[mid]
        elif nums[l] < nums[r]:
            return nums[l]
        elif nums[mid] == nums[l]:
            l += 1
        elif nums[mid] <= nums[r]:
            r = mid - 1
        else:
            l = mid + 1

    return nums[r]


if __name__ == "__main__":
    nums = [1, 3, 3, 0, 0, 0]
    print(findMin(nums))
