# https://leetcode.com/problems/largest-rectangle-in-histogram/


def largestRectangleArea(heights: list[int]) -> int:
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            pre_h = heights[stack.pop(-1)]

            while stack and heights[stack[-1]] == pre_h:
                stack.pop(-1)

            if stack:
                length = i - stack[-1] - 1
            else:
                length = i

            max_area = max(max_area, pre_h * length)

        stack.append(i)

    size = len(heights)
    while stack:
        pre_h = heights[stack.pop(-1)]

        while stack and heights[stack[-1]] == pre_h:
            stack.pop(-1)

        if stack:
            length = size - stack[-1] - 1
        else:
            length = size

        max_area = max(max_area, pre_h * length)

    return max_area


if __name__ == "__main__":
    heights = [5, 4, 1, 2]
    print(largestRectangleArea(heights))
