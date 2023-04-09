# https://leetcode.com/problems/path-sum/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root: TreeNode, targetSum: int):

    def DLR(node: TreeNode, cur_sum: int, hasPath: bool):
        if node is None or hasPath:
            return hasPath
        # must be leaf
        if cur_sum + node.val == targetSum and not node.left and not node.right:
            hasPath = True
            return hasPath

        hasPath = DLR(node.left, cur_sum + node.val, hasPath)
        hasPath = DLR(node.right, cur_sum + node.val, hasPath)

    hasPath = DLR(root, 0, False)
    return hasPath
