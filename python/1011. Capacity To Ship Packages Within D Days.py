# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/


def shipWithinDays(weights: list[int], days: int) -> int:

    def check(x: int):

        total, cnt = 0, 1

        for w in weights:
            if w > x:
                return False
            if total + w > x:
                cnt += 1
                total = w
            else:
                total += w

        return cnt <= days

    l, r = max(weights), sum(weights)

    while l < r:
        mid = int(l + (r - l) / 2)

        if check(mid):
            r = mid
        else:
            l = mid + 1

    return l
