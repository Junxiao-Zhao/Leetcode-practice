# https://leetcode.com/problems/reverse-linked-list/


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode):
    if head is None:
        return []

    def reverse(cur: ListNode, pre: ListNode):
        next = cur.next
        cur.next = pre
        if next is None:
            return cur
        return reverse(next, cur)

    return reverse(head, None)
