# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/


def checkPowersOfThree(n: int):
    while n > 0:
        if n % 3 == 2:
            return False
        n //= 3
    return True
