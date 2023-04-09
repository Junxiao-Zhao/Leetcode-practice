# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
def take_finish(interval: list):
    return interval[1]


def findMinArrowShots(points: list):
    points.sort(key=take_finish)

    i = 0
    j = 1
    count = 1
    while (j < len(points)):
        if (points[i][1] < points[j][0]):
            count += 1
            i = j
        j += 1
    return count
