# https://leetcode.com/problems/partition-labels/
def take_start(interval: list):
    return interval[0]


def __partitionLabels(s: str):
    intervals = dict()

    for i in range(len(s)):
        intervals.setdefault(s[i], [i, i])
        intervals[s[i]][1] = i

    intervals = sorted(intervals.values(), key=take_start)

    cur_start = 0
    cur_last = intervals[0][1]
    count = list()
    for j in range(len(intervals) - 1):
        if cur_last < intervals[j + 1][0]:
            count.append(cur_last - cur_start + 1)
            cur_start = intervals[j + 1][0]
            cur_last = intervals[j + 1][1]
        elif intervals[j + 1][1] > cur_last:
            cur_last = intervals[j + 1][1]
    count.append(cur_last - cur_start + 1)

    return count


def partitionLabels(s: str):
    domain = dict()

    for i, each in enumerate(s):
        domain.setdefault(each, [i, i])
        domain[each][1] = i

    domain = list(domain.values())
    domain.sort(key=lambda x: x[0])

    ans = []
    end_time = 0
    pre_start = 0
    for start, end in domain:
        if start > end_time:
            ans.append(end_time - pre_start + 1)
            pre_start = start
            end_time = end
        else:
            end_time = max(end_time, end)

    ans.append(len(s) - pre_start)
    return ans


if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    print(partitionLabels(s))
