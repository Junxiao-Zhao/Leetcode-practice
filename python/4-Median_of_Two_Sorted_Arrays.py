# https://leetcode.com/problems/median-of-two-sorted-arrays/

import math


def findMedianSortedArrays(nums1: list, nums2: list):
    total_len = len(nums1) + len(nums2)
    is_odd = total_len % 2
    k = math.ceil(total_len / 2)

    def getKthElement(k):
        offset_l = offset_r = 0

        while True:
            if offset_l >= len(nums1):
                return nums2[offset_r + k - 1]
            if offset_r >= len(nums2):
                return nums1[offset_l + k - 1]
            if k == 1:
                return min(nums1[offset_l], nums2[offset_r])

            cur = k // 2 - 1

            index_l = min(cur + offset_l, len(nums1) - 1)
            index_r = min(cur + offset_r, len(nums2) - 1)
            if nums1[index_l] <= nums2[index_r]:
                k -= index_l - offset_l + 1
                offset_l += cur + 1
            else:
                k -= index_r - offset_r + 1
                offset_r += cur + 1

    if is_odd:
        return getKthElement(k)
    else:
        return (getKthElement(k) + getKthElement(k + 1)) / 2


if __name__ == "__main__":
    nums1 = [1]
    nums2 = [2, 3, 4, 5, 6]
    print(findMedianSortedArrays(nums1, nums2))
