# https://leetcode.com/problems/reverse-only-letters/


def reverseOnlyLetters(s: str):
    i, j = 0, len(s) - 1

    while i < j:
        if not s[i].isalpha() or not s[j].isalpha():
            if not s[i].isalpha():
                i += 1
            if not s[j].isalpha():
                j -= 1
        else:
            s = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
            i += 1
            j -= 1

    return s
