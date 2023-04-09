# https://leetcode.com/problems/interleaving-string/


def isInterleave(s1: str, s2: str, s3: str):

    if len(s3) != len(s1) + len(s2):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if j > 0 and s3[i + j - 1] == s2[j - 1]:
                dp[i][j] |= dp[i][j - 1]
            if i > 0 and s3[i + j - 1] == s1[i - 1]:
                dp[i][j] |= dp[i - 1][j]

    return dp[-1][-1]


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(isInterleave(s1, s2, s3))
