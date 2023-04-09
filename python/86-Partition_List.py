# https://leetcode.com/problems/partition-list/


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head: ListNode, x: int):

    cur = head
    pre = start = pre_start = None
    found = False

    while cur is not None:

        if not found and cur.val >= x:
            start = cur
            pre_start = pre
            found = True

        if start is not None and cur.val < x:
            pre.next = cur.next
            cur.next = start
            if pre_start is not None:
                pre_start.next = cur
            else:
                head = cur
            pre_start = cur
            cur = pre.next
        else:
            pre = cur
            cur = cur.next

    return head
