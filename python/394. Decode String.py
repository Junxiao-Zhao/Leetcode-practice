# https://leetcode.com/problems/decode-string/description/


def decodeString(s: str) -> str:
    k = 0
    encoded_string = ""
    k_stack = []
    str_stack = [""]

    for i in s:
        if i.isdigit():
            k = k * 10 + int(i)
        elif i.isalpha():
            str_stack[-1] += i
        elif i == '[':
            k_stack.append(k)
            k = 0
            str_stack.append("")
        else:
            num = k_stack.pop(-1)
            encoded_string = str_stack.pop(-1)
            str_stack[-1] += num * encoded_string

    return str_stack[0]
