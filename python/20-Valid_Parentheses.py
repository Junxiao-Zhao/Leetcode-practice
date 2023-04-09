# https://leetcode.com/problems/valid-parentheses/


def isValid(s: str):
    store = []
    reverse = dict()
    reverse[')'] = '('
    reverse[']'] = '['
    reverse['}'] = '{'

    for each in s:
        if each in "([{":
            store.append(each)
        else:
            if len(store) and store.pop() == reverse[each]:
                continue
            else:
                return False

    return True if not len(store) else False


if __name__ == "__main__":
    s = "()"
    print(isValid(s))
