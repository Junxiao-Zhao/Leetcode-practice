# https://leetcode.com/problems/koko-eating-bananas/


def minEatingSpeed(piles: list, h: int):
    import numpy as np
    l = np.ceil(sum(piles) / h)
    pre_l = 0

    while True:
        time = sum(np.ceil(each / l) for each in piles)
        if time > h:
            pre_l, l = l, l * 2
        else:
            while pre_l <= l:
                mid = (pre_l + l) // 2
                time = sum(np.ceil(each / mid) for each in piles)
                if time > h:
                    pre_l = mid + 1
                else:
                    l = mid - 1
            return int(pre_l)


if __name__ == "__main__":
    piles = [30, 11, 23, 4, 20]
    print(minEatingSpeed(piles, 5))
