def splitArray(nums: list, k: int) -> int:

    def check(x: int):
        total, cnt = 0, 1

        for n in nums:
            if total + n > x:
                cnt += 1
                total = n
            else:
                total += n

        return cnt <= k

    l = max(nums)
    r = sum(nums)

    while l < r:
        mid = int(l + (r - l) / 2)

        if check(mid):
            r = mid
        else:
            l = mid + 1

    return l


if __name__ == "__main__":
    print(splitArray([1, 2, 3, 4, 5], 2))
