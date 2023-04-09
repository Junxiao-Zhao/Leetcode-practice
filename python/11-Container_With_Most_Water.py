# https://leetcode.com/problems/container-with-most-water/


def maxArea(height: list):
    left, right = 0, len(height) - 1
    vol = (right - left) * min(height[right], height[left])
    i, j = left, right

    while i < j:
        if height[i] <= height[j]:
            i += 1
        else:
            j -= 1
        new_vol = (j - i) * min(height[i], height[j])
        if new_vol > vol:
            vol = new_vol

    return vol
