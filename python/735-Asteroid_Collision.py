# https://leetcode.com/problems/asteroid-collision/


def asteroidCollision(asteroids: list):
    stack = []

    for each in asteroids:
        if each > 0:
            stack.append(each)
        else:
            cur = each
            while stack:
                prev = stack.pop()
                if prev < 0:
                    stack.append(prev)
                    stack.append(cur)
                    cur = 0
                    break
                if prev + cur == 0:
                    cur = 0
                    break
                if prev > -cur:
                    stack.append(prev)
                    cur = 0
                    break
            if cur != 0:
                stack.append(cur)

    return stack


if __name__ == "__main__":
    asteroids = [-2, -1, 1, 2]
    print(asteroidCollision(asteroids))
