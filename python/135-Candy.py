# https://leetcode.com/problems/candy/
def candy():
    scores = [int(s) for s in input("Scores: ").split(" ")]

    count = [1] * len(scores)
    for i in range(1, len(scores)):
        if (scores[i] > scores[i - 1]):
            count[i] = count[i - 1] + 1
    for j in range(0, len(scores) - 1):
        if (scores[j + 1] < scores[j]):
            count[j] = count[j + 1] + 1

    return sum(count)


if __name__ == "__main__":
    print(candy())
