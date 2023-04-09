# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from queue import PriorityQueue


def kSmallestPairs(nums1: list, nums2: list, k: int):
    m, n = len(nums1), len(nums2)
    ans = []
    que = PriorityQueue()
    [que.put((nums1[i] + nums2[0], i, 0)) for i in range(m)]

    while que.qsize() and len(ans) < k:
        _, i, j = que.get()
        ans.append([nums1[i], nums2[j]])
        if j + 1 < n:
            que.put((nums1[i] + nums2[j + 1], i, j + 1))

    return ans


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [1, 2, 3]
    print(kSmallestPairs(nums1, nums2, 10))
