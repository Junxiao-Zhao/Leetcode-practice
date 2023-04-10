# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/


def maxSideLength(mat: list[list[int]], threshold: int) -> int:

    p = [[0] * len(mat[0]) for _ in range(len(mat))]
    p[0][0] = mat[0][0]

    for i in range(1, len(mat)):
        p[i][0] = p[i - 1][0] + mat[i][0]

    for j in range(1, len(mat[0])):
        p[0][j] = p[0][j - 1] + mat[0][j]

    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            p[i][j] = p[i - 1][j] + p[i][j - 1] + mat[i][j] - p[i - 1][j - 1]

    def check(x: int) -> bool:
        for i in range(x - 1, len(mat)):
            for j in range(x - 1, len(mat[i])):
                r = p[i - x][j] if i >= x else 0
                l = p[i][j - x] if j >= x else 0
                u = p[i - x][j - x] if i >= x and j >= x else 0
                total = p[i][j] + u - r - l

                if total <= threshold:
                    return True

        return False

    left, right = 0, min(len(mat), len(mat[0]))

    while left < right:
        mid = int(left + (right - left + 1) / 2)

        if mid == 0 or check(mid):
            left = mid
        else:
            right = mid - 1

    return left


if __name__ == "__main__":
    mat = [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]]
    threshold = 4

    print(maxSideLength(mat, threshold))
