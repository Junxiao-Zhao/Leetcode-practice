# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/


def removeDuplicates(s: str) -> str:
    if len(s) == 1:
        return s

    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(i)

    return "".join(stack)
