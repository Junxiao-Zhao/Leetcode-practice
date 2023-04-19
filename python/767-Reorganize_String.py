# https://leetcode.com/problems/reorganize-string/

from collections import Counter
from queue import PriorityQueue


def reorganizeString(s: str):

    count = Counter(s)
    max_count = max(count.values())
    if max_count > (len(s) + 1) // 2:
        return ""

    que = PriorityQueue()

    for k, v in count.items():
        que.put([-v, k])

    output = []
    while que.qsize() > 1:
        neg_num, char = que.get()
        neg_num2, char2 = que.get()

        output += [char, char2]

        if neg_num < -1:
            que.put([neg_num + 1, char])
        if neg_num2 < -1:
            que.put([neg_num2 + 1, char2])

    if not que.empty():
        _, char = que.get()
        output.append(char)

    return "".join(output)


if __name__ == "__main__":
    s = "vvvlo"
    print(reorganizeString(s))
