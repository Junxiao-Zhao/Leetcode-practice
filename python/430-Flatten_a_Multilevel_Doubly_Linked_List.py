# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


class Node:

    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self) -> str:
        return str(self.val)


def flatten(head: Node):

    def to_flat(head: Node):

        head.next = head.child
        head.child.prev = head
        head.child = None

        cur = head.next
        prev = head
        while cur:
            if cur.child:
                cur_next = cur.next
                last = to_flat(cur)
                last.next = cur_next
                if cur_next:
                    cur_next.prev = last
                cur = cur_next
                prev = last
            else:
                prev = cur
                cur = cur.next

        return prev

    cur = head
    while cur:
        if cur.child:
            cur_next = cur.next
            last = to_flat(cur)
            last.next = cur_next
            if cur_next:
                cur_next.prev = last
            cur = cur_next
        else:
            cur = cur.next

    return head


if __name__ == "__main__":
    level1 = [1]
    level2 = [2]
    level3 = [3]

    levels = [level1, level2, level3]

    for i in range(len(levels)):
        for j in range(len(levels[i])):
            levels[i][j] = Node(levels[i][j], None, None, None)

    for i in range(len(levels)):
        for j in range(len(levels[i])):
            levels[i][j].prev = levels[i][j - 1] if j > 0 else None
            levels[i][j].next = levels[i][
                j + 1] if j < len(levels[i]) - 1 else None
    levels[0][0].child = levels[1][0]
    levels[1][0].child = levels[2][0]

    head = flatten(levels[0][0])
    while head:
        print(head)
        head = head.next
