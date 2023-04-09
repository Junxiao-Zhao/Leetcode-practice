# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/


def findLongestWord(s: str, dictionary: list):
    table = [[0] * 26 for _ in range(len(s))]
    table.append([len(s)] * 26)

    for i in range(len(s) - 1, -1, -1):
        for j in range(26):
            if s[i] == chr(j + 97):
                table[i][j] = i
            else:
                table[i][j] = table[i + 1][j]

    res = ""
    for t in dictionary:
        match = True
        j = 0
        for i in range(len(t)):
            if table[j][ord(t[i]) - 97] == len(s):
                match = False
                break
            j = table[j][ord(t[i]) - 97] + 1

        if match:
            if len(t) > len(res) or (len(t) == len(res) and t < res):
                res = t

    return res


if __name__ == "__main__":
    s = "abpcplea"
    dic = [
        "ale", "apple", "monkey", "plea", "abpcplaaa", "abpcllllll",
        "abccclllpppeeaaaa"
    ]
    print(findLongestWord(s, dic))
