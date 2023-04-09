# https://leetcode.com/problems/minimum-depth-of-binary-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root: TreeNode):
    if not root:
        return 0
    count = 1000000

    def dfs(node: TreeNode, depth: int):
        nonlocal count
        depth += 1
        if not node:
            return
        if not node.left and not node.right:
            if depth < count:
                count = depth
            return
        dfs(node.left, depth)
        dfs(node.right, depth)

    dfs(root, 0)
    return count
