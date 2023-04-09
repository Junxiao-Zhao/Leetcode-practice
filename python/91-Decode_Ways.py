# https://leetcode.com/problems/decode-ways/


def numDecodings(s: str):

    dp = [0] * len(s)
    dp[-1] = 1 if s[-1] != '0' and int(s[-1]) >= 1 and int(s[-1]) <= 26 else 0
    dp.append(1)

    for i in range(len(s) - 2, -1, -1):
        if s[i] == '0':
            continue
        if int(s[i]) >= 1 and int(s[i]) <= 26:
            dp[i] += dp[i + 1]
        if int(s[i:i + 2]) >= 1 and int(s[i:i + 2]) <= 26:
            dp[i] += dp[i + 2]

    return dp[0]


if __name__ == "__main__":
    s = "226"
    print(numDecodings(s))
