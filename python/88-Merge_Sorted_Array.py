# https://leetcode.com/problems/merge-sorted-array/


def merge(nums1, m, nums2, n):

    cp1 = nums1[:m]
    i = j = 0
    while (i < m and j < n):
        if cp1[i] <= nums2[j]:
            nums1[i + j] = cp1[i]
            i += 1
        else:
            nums1[i + j] = nums2[j]
            j += 1

    nums1[i + j:] = cp1[i:] if i < m else nums2[j:]
