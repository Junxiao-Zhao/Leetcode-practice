# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from queue import PriorityQueue


def kthSmallest(matrix: list, k: int):
    que = PriorityQueue()
    [que.put((matrix[i][0], i, 0)) for i in range(len(matrix))]

    ans = None
    while k > 0:
        ans, i, j = que.get()
        if j + 1 < len(matrix[0]):
            que.put((matrix[i][j + 1], i, j + 1))
        k -= 1

    return ans


if __name__ == "__main__":
    martix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22],
              [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    print(kthSmallest(martix, 5))
