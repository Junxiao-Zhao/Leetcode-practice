# https://leetcode.com/problems/count-good-nodes-in-binary-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode):
    if not root:
        return 0

    count = 0

    def dfs(node: TreeNode, path_max: int):
        if not node:
            return
        nonlocal count
        if node.val >= path_max:
            count += 1
            path_max = node.val
        dfs(node.left, path_max)
        dfs(node.right, path_max)

    dfs(root, -100000)
    return count
