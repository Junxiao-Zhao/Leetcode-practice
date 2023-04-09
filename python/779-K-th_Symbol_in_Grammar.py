# https://leetcode.com/problems/k-th-symbol-in-grammar/


def kthGrammar(n: int, k: int):
    k -= 1
    res = 0
    while k:
        k &= k - 1
        res ^= 1
    return res


if __name__ == "__main__":
    print(kthGrammar(4, 8))
