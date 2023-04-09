# https://leetcode.com/problems/validate-binary-search-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode):

    def LDR(node: TreeNode, isValid: bool):
        if not node or not isValid:
            return isValid

        isValid = LDR(node.left, isValid)
        nonlocal last_val
        if last_val is not None and node.val <= last_val:
            return False
        last_val = node.val
        isValid = LDR(node.right, isValid)
        return isValid

    last_val = 0
    return LDR(root, True)
