# https://leetcode.com/problems/gas-station/


def canCompleteCircuit(gas: list, cost: list):
    if sum(gas) < sum(cost):
        return -1

    i = 0
    while i < len(gas):
        if gas[i] >= cost[i]:
            tank = 0
            for j in range(i, i + len(gas) - 1):
                tank += gas[j % len(gas)] - cost[j % len(gas)]
                if tank < 0:
                    i = j
                    break
            if tank >= 0:
                return i
        else:
            i += 1

    return -1


if __name__ == "__main__":
    gas = [5, 1, 2, 3, 4]
    cost = [4, 4, 1, 5, 1]
    print(canCompleteCircuit(gas, cost))
