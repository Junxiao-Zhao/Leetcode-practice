# https://leetcode.com/problems/binary-tree-inorder-traversal/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    ans = list()
    stack = list()

    while root or len(stack) > 0:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        ans.append(root.val)
        root = root.right

    return ans
