# https://leetcode.com/problems/climbing-stairs/


def climbStairs(n: int):
    store = [1, 2]

    for i in range(2, n):
        store.append(store[i - 1] + store[i - 2])

    return store[n - 1]


if __name__ == "__main__":
    print(climbStairs(3))
