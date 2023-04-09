# https://leetcode.com/problems/minimum-window-substring/


def minWindow(s: str, t: str) -> str:
    count = [0] * (122 - 64)
    flag = [0] * (122 - 64)

    for e in t:
        flag[ord(e) - 65] = True
        count[ord(e) - 65] += 1

    size = 0
    l = 0
    min_size = len(s) + 1

    for r in range(len(s)):
        if flag[ord(s[r]) - 65]:
            count[ord(s[r]) - 65] -= 1

            if count[ord(s[r]) - 65] >= 0:
                size += 1

        while size == len(t):
            if r - l + 1 < min_size:
                min_size = r - l + 1
                min_l = l

            if flag[ord(s[l]) - 65]:
                count[ord(s[l]) - 65] += 1
                if count[ord(s[l]) - 65] > 0:
                    size -= 1

            l += 1

    return "" if min_size > len(s) else s[min_l:min_l + min_size]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))
