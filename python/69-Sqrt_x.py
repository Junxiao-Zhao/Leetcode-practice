# https://leetcode.com/problems/sqrtx/


def binary(x: int, start: int, end: int):
    mid = (start + end) // 2

    if mid**2 <= x and (mid + 1)**2 > x:
        return mid
    elif mid**2 < x:
        return binary(x, mid + 1, end)
    else:
        return binary(x, start, mid - 1)


def mySqrt(x: int):
    i = 1

    while i**2 < x:
        i *= 2

    return binary(x, i // 2, i)


if __name__ == "__main__":
    print(mySqrt(7))
