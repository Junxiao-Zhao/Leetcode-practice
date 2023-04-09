# https://leetcode.com/problems/linked-list-cycle/


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: ListNode):
    a, b = head, head

    while b.next:
        a = a.next
        b = b.next.next
        if a == b:
            return True

    return False
