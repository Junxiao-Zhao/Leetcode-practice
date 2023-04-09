# https://leetcode.com/problems/palindrome-partitioning/


def partition(s: str):
    palin_table = [[0] * len(s) for _ in range(len(s))]

    def isPalin(i: int, j: int):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    ans = []

    for i in range(len(s)):
        j = i
        while j < len(s):
            if isPalin(i, j):
                palin_table[i][j] = 1
            j += 1

    def find_partition(index: int, cur: list):
        if index >= len(s):
            ans.append(cur)
            return
        for i in range(len(s)):
            if palin_table[index][i]:
                temp = cur.copy()
                temp.append(s[index:i + 1])
                find_partition(i + 1, temp)

    find_partition(0, [])
    return ans


if __name__ == "__main__":
    s = "aab"
    print(partition(s))
