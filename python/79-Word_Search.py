# https://leetcode.com/problems/word-search/


def exist(board: list, word: str):
    m = len(board)
    n = len(board[0])
    visited = [[0] * n for _ in range(m)]
    find = False

    def backtracking(i: int, j: int, find: bool, board: list, visited: list,
                     pos: int, word: str):
        if (i < 0 or i >= m or j < 0 or j >= n):
            return find
        if (visited[i][j] or find or board[i][j] != word[pos]):
            return find
        if pos == len(word) - 1:
            find = True
            return find

        trick = [-1, 0, 1, 0, -1]
        visited[i][j] = 1
        for k in range(4):
            x = i + trick[k]
            y = j + trick[k + 1]
            find = backtracking(x, y, find, board, visited, pos + 1, word)
        visited[i][j] = 0

        return find

    for a in range(m):
        for b in range(n):
            find = backtracking(a, b, find, board, visited, 0, word)

    return find


if __name__ == "__main__":
    board = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
             ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
    word = "AAAAAAAAAAAAABB"
    print(exist(board, word))
