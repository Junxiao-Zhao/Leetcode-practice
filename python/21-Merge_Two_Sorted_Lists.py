# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode):

    if list1 is None:
        return list2
    if list2 is None:
        return list1

    cur1 = list1
    cur2 = list2
    head = None
    pre = head
    while cur1 is not None and cur2 is not None:
        if cur1.val <= cur2.val:
            small = cur1
            large = cur2
        else:
            small = cur2
            large = cur1
        if head is None:
            head = small
        else:
            pre.next = small
        pre = small
        cur1 = small.next
        cur2 = large

    if cur1 is None:
        pre.next = cur2
    else:
        pre.next = cur1

    return head
