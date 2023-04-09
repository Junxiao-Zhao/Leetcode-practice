# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def findMin(nums: list):
    if nums[0] <= nums[-1]:
        return nums[0]

    n = len(nums)
    l, r = 0, n - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= nums[mid - 1] and nums[mid] <= nums[(mid + 1) % n]:
            return nums[mid]
        elif nums[mid] >= nums[l] and nums[mid] >= nums[r]:
            l = mid + 1
        elif nums[mid] <= nums[l] and nums[mid] <= nums[r]:
            r = mid - 1
        else:
            return nums[l]

    return nums[l]
