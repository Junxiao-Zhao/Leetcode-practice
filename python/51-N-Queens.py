# https://leetcode.com/problems/n-queens/
# https://leetcode.cn/problems/n-queens/solution/nhuang-hou-by-leetcode-solution/


def solveNQueens(n: int):
    chessboard = [[0] * n for _ in range(n)]
    ans = list()

    def backtracking(k: int, pos: list):
        if k == 0:
            ans.append(pos)
            return

        for i in range(n):
            if chessboard[n - k][i] == 0:
                chessboard[n - k][i] += 1
                cur_pos = pos.copy()
                cur_pos.append("." * (i) + "Q" + "." * (n - i - 1))
                for j in range(n - k + 1, n):
                    chessboard[j][i] += 1
                    if i + j - (n - k) < n:
                        chessboard[j][i + j - (n - k)] += 1
                    if i - (j - (n - k)) >= 0:
                        chessboard[j][i - (j - (n - k))] += 1
                backtracking(k - 1, cur_pos)
                chessboard[n - k][i] -= 1
                for j in range(n - k + 1, n):
                    chessboard[j][i] -= 1
                    if i + j - (n - k) < n:
                        chessboard[j][i + j - (n - k)] -= 1
                    if i - (j - (n - k)) >= 0:
                        chessboard[j][i - (j - (n - k))] -= 1

    backtracking(n, [])
    return ans


if __name__ == "__main__":
    print(solveNQueens(5))
