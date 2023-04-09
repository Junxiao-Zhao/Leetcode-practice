# https://leetcode.com/problems/next-greater-node-in-linked-list/


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nextLargerNodes(head: ListNode):
    stack = list()
    ans = list()

    node = head
    index = 0
    while node:
        while stack:
            if stack[-1][1] >= node.val:
                break
            else:
                i, _ = stack.pop()
                ans[i] = node.val
        stack.append((index, node.val))
        node = node.next
        ans.append(0)
        index += 1

    return ans
