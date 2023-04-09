# https://leetcode.com/problems/non-overlapping-intervals/
def take_finish(interval: list):
    return interval[1]


def non_over_intvl(intervals: list):
    intervals.sort(key=take_finish)

    last = intervals[0]
    count = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] < last[1]:
            count += 1
        else:
            last = intervals[i]

    return count


if __name__ == "__main__":
    intvls = [[1, 2], [2, 4], [1, 3]]
    print(non_over_intvl(intvls))
