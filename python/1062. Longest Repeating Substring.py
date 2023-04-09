# https://leetcode.ca/2018-10-27-1062-Longest-Repeating-Substring/

def f(s: str, length: int) -> int:
    have = set()

    for i in range(0, len(s) - length + 1):

        if s[i: i+length] in have:
            return True
        have.add(s[i: i+length])

    return False


def longestRepeatingSubstring(s: str) -> int:
    l, r = 0, len(s) - 1

    while l < r:
        mid = int(l + (r - l + 1) / 2)

        if f(s, mid):
            l = mid
        else:
            r = mid - 1

    return l


if __name__ == "__main__":
    s = "aaaaa"
    print(longestRepeatingSubstring(s))
