# https://leetcode.com/problems/trapping-rain-water/description/


def trap(height: list[int]) -> int:
    i, j = 1, len(height) - 2
    left_max, right_max = 0, 0
    total = 0

    for _ in range(1, len(height) - 1):
        if height[i - 1] < height[j + 1]:
            left_max = max(left_max, height[i - 1])
            total += left_max - height[i] if left_max > height[i] else 0
            i += 1
        else:
            right_max = max(right_max, height[j + 1])
            total += right_max - height[j] if right_max > height[j] else 0
            j -= 1

    return total
