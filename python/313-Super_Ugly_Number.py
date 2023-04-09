# https://leetcode.com/problems/super-ugly-number/


def nthSuperUglyNumber(n: int, primes: list):
    dp = [0] * (n + 1)
    m = len(primes)
    pointers = [0] * m
    nums = [1] * m

    for i in range(1, n + 1):
        min_num = min(nums)
        dp[i] = min_num
        for j in range(m):
            if nums[j] == min_num:
                pointers[j] += 1
                nums[j] = dp[pointers[j]] * primes[j]

    return dp[n]


if __name__ == "__main__":
    primes = [2, 7, 13, 19]
    print(nthSuperUglyNumber(12, primes))
