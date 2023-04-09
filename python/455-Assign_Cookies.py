# https://leetcode.com/problems/assign-cookies/
def assign_cookies():

    children = input("Hungry values: ")
    cookies = input("Cookie sizes: ")

    children = sorted([int(h) for h in children.split(" ")])
    cookies = sorted([int(c) for c in cookies.split(" ")])

    count = 0
    child_index = 0
    cookie_index = 0
    while (child_index < len(children) and cookie_index < len(cookies)):
        if (cookies[cookie_index] >= children[child_index]):
            count += 1
            child_index += 1
        cookie_index += 1

    return count


if __name__ == "__main__":
    print(assign_cookies())
