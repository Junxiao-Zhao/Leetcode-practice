# https://leetcode.com/problems/longest-common-prefix/


def longestCommonPrefix(strs: list):
    if len(strs) == 1:
        return strs[0]
    max_len = min([len(each) for each in strs])

    count = dict()
    for i in range(max_len):
        for each in strs:
            count.setdefault(each[i], 0)
        if len(count.values()) > 1:
            return strs[0][:i]
        count.clear()

    return strs[0][:max_len]


if __name__ == "__main__":
    strs = ["baac", "acb", "bacc", "cb"]
    print(longestCommonPrefix(strs))
