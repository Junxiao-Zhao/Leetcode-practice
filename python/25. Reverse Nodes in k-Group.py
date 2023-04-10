# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

from utils import ListNode


def reverseKGroup(head: ListNode, k: int) -> ListNode:
    cnt = 0
    node = head
    reverse_head = [head]
    while node:
        node = node.next
        cnt += 1
        if cnt % k == 0:
            reverse_head.append(node)

    start = ListNode(next=head)
    pre_node = start

    def reverse(node, num, pre):
        if num == k:
            pre.next = node
            return

        reverse(node.next, num + 1, pre)
        node.next.next = node

    for h in reverse_head:
        if cnt < k:
            pre_node.next = h
            break

        reverse(h, 1, pre_node)
        pre_node = h
        cnt -= k

    return start.next
