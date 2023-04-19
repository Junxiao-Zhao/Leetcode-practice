# https://leetcode.com/problems/next-greater-element-i/description/


def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    stack = list()
    nums2_dic = dict()

    for i in range(len(nums2) - 1, -1, -1):
        while stack and stack[-1] < nums2[i]:
            stack.pop(-1)

        nums2_dic[nums2[i]] = -1 if not stack else stack[-1]
        stack.append(nums2[i])

    return [nums2_dic[j] for j in nums1]
