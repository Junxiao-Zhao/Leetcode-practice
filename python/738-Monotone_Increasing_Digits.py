# https://leetcode.com/problems/monotone-increasing-digits/


def monotoneIncreasingDigits(n: int):
    n = list(str(n))
    result = ""
    for i in range(len(n) - 1, -1, -1):
        if (ord(n[i]) >= ord(n[i - 1]) if i > 0 else True):
            result = n[i] + result
        else:
            n[i - 1] = chr(ord(n[i - 1]) - 1)
            result = '9' * (len(result) + 1)

    return int(result)


if __name__ == "__main__":
    print(monotoneIncreasingDigits(10))
