# https://leetcode.com/problems/rotate-list/


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def rotateRight(head: ListNode, k: int):
    if head is None:
        return head

    count = 1
    cur = head
    while cur.next is not None:
        count += 1
        cur = cur.next

    k = count - k % count
    cur.next = head

    for i in range(k):
        cur = cur.next
    head = cur.next
    cur.next = None

    return head
