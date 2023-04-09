# https://leetcode.com/problems/linked-list-cycle-ii/


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: ListNode):
    a = b = head

    while True:
        if a is None or a.next is None:
            return None
        a = a.next.next
        b = b.next

        if a == b:
            break

    a = head
    while (a != b):
        a = a.next
        b = b.next

    return a
