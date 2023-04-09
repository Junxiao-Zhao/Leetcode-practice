# https://leetcode.com/problems/reverse-linked-list-ii/


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def reverseBetween(head: ListNode, left: int, right: int):
    if left == right:
        return head
    count = 0
    cur = head
    pre = None
    r_head = r_tail = None
    s_tail = None
    while count < right:
        count += 1
        if count == left - 1:
            s_tail = cur
        if count == left:
            r_tail = cur
        if count >= left and count < right:
            r_head = cur.next
            cur.next = pre
            pre = cur
            cur = r_head
        elif count == right:
            cur = r_head.next
            r_head.next = pre

        else:
            pre = cur
            cur = cur.next

    r_tail.next = cur
    if s_tail is not None:
        s_tail.next = r_head
        return head
    else:
        return r_head
