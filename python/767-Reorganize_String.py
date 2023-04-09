# https://leetcode.com/problems/reorganize-string/


def reorganizeString(s: str):
    from collections import Counter
    import numpy as np

    counts = Counter(s)
    max_exec = max(counts.values())
    max_count = sum(1 for i in counts.values() if i == max_exec)

    if (max_exec - 1) * 2 + max_count > len(s):
        return ""

    else:
        letters = [
            list(each) for each in sorted(
                counts.items(), key=lambda x: x[1], reverse=True)
        ]

        ans = []
        for i in range(max_count):
            ans.append([letters[i][0]] * max_exec)

        temp = []
        for i in range(max_count, len(letters)):
            temp += [letters[i][0]] * letters[i][1]

        for j in range(0, len(temp), max_exec - 1):
            ans.append(temp[j:j + max_exec - 1])
            ans[-1] += [""] * (max_exec - len(ans[-1]))

        ans = np.array(ans).T
        answer = ""
        for row in ans:
            for col in row:
                answer += col
        return answer


if __name__ == "__main__":
    s = "vvvlo"
    print(reorganizeString(s))
