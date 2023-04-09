# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/


def lsk(s: str, k: int):
    count = [0] * 26

    l = 0
    output = 0
    num = 0
    length = 0
    for r in range(len(s)):
        if count[ord(s[r]) - 97] == 0:
            num += 1
        count[ord(s[r]) - 97] += 1
        length += 1

        while (num > k):
            count[ord(s[l]) - 97] -= 1
            if count[ord(s[l]) - 97] == 0:
                num -= 1
            l += 1
            length -= 1

        if output < length:
            output = length

    return output


if __name__ == "__main__":
    s = "aa"
    print(lsk(s, 1))
