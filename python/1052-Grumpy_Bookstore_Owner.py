# https://leetcode.com/problems/grumpy-bookstore-owner/


def maxSatisfied(customers: list, grumpy: list, minutes: int):
    without_secret = sum(
        (customers[i] if grumpy[i] == 0 else 0) for i in range(len(grumpy)))

    l, r = 0, minutes
    max_secret = 0
    cur_secret = sum(customers[i] if grumpy[i] else 0 for i in range(minutes))

    while r <= len(grumpy):
        max_secret = max(max_secret, cur_secret)
        if grumpy[l]:
            cur_secret -= customers[l]
        l += 1
        if r < len(grumpy) and grumpy[r]:
            cur_secret += customers[r]
        r += 1

    return without_secret + max_secret
