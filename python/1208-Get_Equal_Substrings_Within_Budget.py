# https://leetcode.com/problems/get-equal-substrings-within-budget/


def equalSubstring(s: str, t: str, maxCost: int):
    l = r = 0
    curCost = 0
    cur_len = max_len = 0

    while r < len(t):
        cur_len += 1
        curCost += abs(ord(s[r]) - ord(t[r]))
        if curCost <= maxCost:
            max_len = max(max_len, cur_len)
        else:
            curCost -= abs(ord(s[l]) - ord(t[l]))
            cur_len -= 1
            l += 1

        r += 1

    return max_len


if __name__ == "__main__":
    s = "krrgw"
    t = "zjxss"
    print(equalSubstring(s, t, 19))
