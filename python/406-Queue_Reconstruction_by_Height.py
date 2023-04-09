# https://leetcode.com/problems/queue-reconstruction-by-height/
from operator import itemgetter


def reconstructQueue(people: list[int]):
    people.sort(key=itemgetter(0, 1))

    for i in range(len(people) - 1, -1, -1):
        j = i - 1
        count = people[i][1]

        while (j >= 0 and people[j][0] >= people[i][0]):
            count -= 1
            j -= 1

        if count > 0:
            cur = people[i]
            for k in range(i, i + count):
                people[k] = people[k + 1]
            people[i + count] = cur

    return people


if __name__ == "__main__":
    print(
        reconstructQueue([[3, 0], [6, 0], [5, 2], [7, 0], [3, 4], [5, 3],
                          [6, 2], [2, 7], [9, 0], [1, 9]]))
