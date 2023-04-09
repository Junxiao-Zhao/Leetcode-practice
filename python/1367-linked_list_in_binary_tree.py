# https://leetcode.com/problems/linked-list-in-binary-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def isSubPath(head: ListNode, root: TreeNode):
    findSub = False

    def DLR(tree_node: TreeNode, list_node: ListNode):
        nonlocal findSub
        if not list_node:
            findSub = True
            return
        if not tree_node:
            return

        if tree_node.val == list_node.val:
            DLR(tree_node.left, list_node.next)
            DLR(tree_node.right, list_node.next)

    stack = [root]

    while len(stack) > 0 and not findSub:
        cur = stack.pop(0)

        if cur:
            stack.append(cur.left)
            stack.append(cur.right)
            if cur.val == head.val:
                DLR(cur, head)

    return findSub
