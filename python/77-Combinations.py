# https://leetcode.com/problems/combinations/


def backtracking(s: int, n: int, k: int, ans: list, temp: list):
    if k == 0:
        ans.append(temp.copy())
        return

    for i in range(s, n + 1):
        a = temp.copy()
        a.append(i)
        backtracking(i + 1, n, k - 1, ans, a)


def combine(n: int, k: int):
    ans = []
    backtracking(1, n, k, ans, [])
    return ans


if __name__ == "__main__":
    print(combine(1, 1))
