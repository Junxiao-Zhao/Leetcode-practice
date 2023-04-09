# https://leetcode.ca/all/1231.html


def maximizeSweetness(sweetness: list, k: int):

    def check(x: int):
        total, cnt = 0, 0

        for s in sweetness:
            total += s
            if total >= x:
                cnt += 1
                total = 0

        return cnt > k

    l = min(sweetness)
    r = sum(sweetness)

    while l < r:
        mid = int(l + (r - l + 1) / 2)

        if check(mid):
            l = mid
        else:
            r = mid - 1

    return l


if __name__ == "__main__":
    print(maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2))
