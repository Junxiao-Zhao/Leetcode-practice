# https://leetcode.com/problems/permutation-in-string/


def checkInclusion(s1: str, s2: str):
    import collections
    count1 = collections.Counter(s1)
    count2 = collections.Counter(s2[:len(s1)])

    l, r = 0, len(s1)

    while r <= len(s2):
        found = True
        for key, val in count2.items():
            if count1.get(key, -1) != val:
                found = False
                break
        if found:
            return True
        if r == len(s2):
            break
        count2[s2[l]] -= 1
        if count2[s2[l]] == 0:
            del count2[s2[l]]
        l += 1
        count2.setdefault(s2[r], 0)
        count2[s2[r]] += 1
        r += 1

    return False


if __name__ == "__main__":
    s1 = "adc"
    s2 = "dcda"
    print(checkInclusion(s1, s2))
