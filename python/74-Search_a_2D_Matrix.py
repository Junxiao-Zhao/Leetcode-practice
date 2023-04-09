# https://leetcode.com/problems/search-a-2d-matrix/


def searchMatrix(matrix: list, target: int):

    m, n = len(matrix), len(matrix[0])
    l, r = 0, m * n - 1
    i = j = 0
    while l <= r:
        mid = (l + r) // 2
        i = mid // n
        j = mid % n
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            r = mid - 1
        else:
            l = mid + 1

    return False
