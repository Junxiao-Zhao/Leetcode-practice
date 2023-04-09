# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


def maxScore(cardPoints: list, k: int):
    max_point = 0
    l, r = len(cardPoints) - k, len(cardPoints) - 1
    cur_point = sum(cardPoints[l:r + 1])

    for i in range(k + 1):
        max_point = max(max_point, cur_point)
        cur_point -= cardPoints[l % len(cardPoints)]
        l += 1
        r += 1
        cur_point += cardPoints[r % len(cardPoints)]

    return max_point


if __name__ == "__main__":
    cards = [96, 90, 41, 82, 39, 74, 64, 50, 30]
    print(maxScore(cards, 8))
