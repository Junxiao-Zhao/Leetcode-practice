# https://leetcode.com/problems/remove-linked-list-elements/


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: ListNode, val: int):
    cur = head
    pre = None
    while cur is not None:
        if cur.val == val:
            if pre is None:
                head = cur.next
                cur.next = None
                cur = head
            else:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
        else:
            pre = cur
            cur = cur.next

    return head
