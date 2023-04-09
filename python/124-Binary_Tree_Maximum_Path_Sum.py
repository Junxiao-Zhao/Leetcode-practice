# https://leetcode.com/problems/binary-tree-maximum-path-sum/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode):
    max_path = dict()
    largest = -1001

    def LRD(node: TreeNode):
        if not node:
            max_path[node] = 0
            return
        nonlocal largest
        LRD(node.left)
        LRD(node.right)
        left_max = max_path[node.left] if max_path[node.left] > 0 else 0
        right_max = max_path[node.right] if max_path[node.right] > 0 else 0
        max_path[node] = max(left_max, right_max, 0) + node.val
        if left_max + right_max + node.val > largest:
            largest = left_max + right_max + node.val

    LRD(root)
    return largest
