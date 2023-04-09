# https://leetcode.com/problems/restore-ip-addresses/


def backtracking(s: str, ans: list, pos: int, cur_ip: str, depth: int):

    if pos == len(s) and depth == 4:
        ans.append(cur_ip[:-1])
        return

    elif depth <= 3 and pos < len(s):
        pre_digit = ''
        for i in range(3 if len(s) - pos >= 3 else len(s) - pos):
            pre_digit += s[pos + i]
            if pre_digit[0] == '0' and i != 0:
                break
            int_digit = int(pre_digit)
            if int_digit < 0 or int_digit > 255:
                break
            if len(s) - pos - i - 1 > (3 - depth) * 3:
                continue
            new_ip = cur_ip
            new_ip += pre_digit + '.'
            backtracking(s, ans, pos + i + 1, new_ip, depth + 1)


def restoreIpAddresses(s: str):
    ans = []
    if len(s) <= 12 and s.isdigit():
        backtracking(s, ans, 0, '', 0)
    return ans


if __name__ == "__main__":
    s = "101023"
    print(restoreIpAddresses(s))
