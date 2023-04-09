# https://leetcode.com/problems/sum-of-square-numbers/
import math


def judgeSquareSum(c: int):
    l = 0
    r = int(math.sqrt(c))

    while l <= r and l**2 + r**2 != c:
        if l**2 + r**2 > c:
            r -= 1
        else:
            l += 1

    return True if l <= r else False
