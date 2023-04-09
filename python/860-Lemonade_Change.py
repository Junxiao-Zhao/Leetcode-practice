# https://leetcode.com/problems/lemonade-change/


def lemonadeChange(bills: list):
    change = {5: 0, 10: 0, 20: 0}
    for each in bills:
        if each > 5:
            rest = each - 5
            for i in [20, 10, 5]:
                amount = min(change[i], rest // i)
                rest -= i * amount
                change[i] -= amount
            if rest != 0:
                return False
        change[each] += 1

    return True


if __name__ == "__main__":
    bills = [5, 5, 10, 10, 20]
    print(lemonadeChange(bills))
