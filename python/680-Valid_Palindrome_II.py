# https://leetcode.com/problems/valid-palindrome-ii/


def palindrome(s: str):
    l = 0
    r = len(s) - 1

    while (l < r):
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1

    return True


def validPalindrome(s: str):
    l = 0
    r = len(s) - 1

    while (l < r):
        if s[l] != s[r]:
            if s[l + 1] == s[r] and s[l] == s[r - 1] and r - l > 1:
                return palindrome(s[l + 1:r + 1]) or palindrome(s[l:r])
            elif s[l + 1] == s[r]:
                return palindrome(s[l + 1:r + 1])
            elif s[l] == s[r - 1]:
                return palindrome(s[l:r])
            else:
                return False
        l += 1
        r -= 1

    return True


if __name__ == "__main__":
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(validPalindrome(s))
