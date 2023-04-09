# https://leetcode.com/problems/evaluate-reverse-polish-notation/


def evalRPN(tokens: list):
    nums = list()
    for each in tokens:
        if each.isalnum() or each[1:].isalnum():
            nums.append(each)
        else:
            num2 = int(nums.pop())
            num1 = int(nums.pop())
            if each == "+":
                result = num1 + num2
            elif each == "-":
                result = num1 - num2
            elif each == "*":
                result = num1 * num2
            else:
                result = int(num1 / num2)
            nums.append(str(result))

    return int(nums.pop())


if __name__ == "__main__":
    tokens = [
        "10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"
    ]
    print(evalRPN(tokens))
