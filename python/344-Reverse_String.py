# https://leetcode.com/problems/reverse-string/


def reverseString(s: list):

    def rev(i, j):
        if i >= j:
            return

        s[i], s[j] = s[j], s[i]
        rev(i + 1, j - 1)

    rev(0, len(s) - 1)

    print(s)


if __name__ == "__main__":
    s = ["H", "a", "n", "n", "a", "h"]
    reverseString(s)
