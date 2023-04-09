# https://leetcode.com/problems/broken-calculator/


def brokenCalc(startValue: int, target: int):
    count = 0
    while target > startValue:
        if target & 1:
            target = (target + 1) // 2
            count += 2
        else:
            target //= 2
            count += 1

    return count + startValue - target


if __name__ == "__main__":
    print(brokenCalc(2, 3))
