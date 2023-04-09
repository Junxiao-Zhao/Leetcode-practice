# https://leetcode.com/problems/longest-repeating-character-replacement/


def characterReplacement(s: str, k: int):
    l, r = 0, 0
    max_len = cur_len = 0
    count = dict()

    while r < len(s):
        count.setdefault(s[r], 0)
        count[s[r]] += 1
        cur_len += 1
        if len(count) <= 1 or cur_len - max(count.values()) <= k:
            max_len = max(max_len, cur_len)
        else:
            count[s[l]] -= 1
            if count[s[l]] == 0:
                del count[s[l]]
            cur_len -= 1
            l += 1
        r += 1

    return max_len


if __name__ == "__main__":
    s = "AABABBA"
    print(characterReplacement(s, 1))
