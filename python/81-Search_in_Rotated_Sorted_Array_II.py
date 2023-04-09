# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/


def binary(nums, l, r):
    while l <= r:
        mid = (l + r) // 2

        if mid != 0 and nums[mid] < nums[mid - 1]:
            return mid
        elif nums[mid] < nums[0]:
            r = mid - 1
        elif nums[mid] > nums[0]:
            l = mid + 1
        else:
            return binary(nums, mid + 1, r) | binary(nums, l, mid - 1)

    return 0


def search(nums: list, target: int):

    if target == nums[0]:
        return True

    pivot = binary(nums, 1, len(nums) - 1)

    if pivot == 0:
        l = 0
        r = len(nums) - 1
    elif target < nums[0]:
        l = pivot
        r = len(nums) - 1
    else:
        l = 0
        r = pivot - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False


if __name__ == "__main__":
    nums = [1, 3]
    print(search(nums, 3))
