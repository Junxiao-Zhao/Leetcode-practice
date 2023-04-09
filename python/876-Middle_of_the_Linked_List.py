# https://leetcode.com/problems/middle-of-the-linked-list/


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: ListNode):
    if head is None:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
