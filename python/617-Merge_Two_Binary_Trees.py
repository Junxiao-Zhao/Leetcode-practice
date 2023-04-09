# https://leetcode.com/problems/merge-two-binary-trees/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTrees(root1: TreeNode, root2: TreeNode):
    if not root1:
        return root2
    if not root2:
        return root1

    def dfs(cur1: TreeNode, cur2: TreeNode, pre1: TreeNode, direct1: str):
        if not cur2:
            return
        if not cur1:
            if direct1 == 'l':
                pre1.left = cur2
            else:
                pre1.right = cur2
            return

        cur1.val += cur2.val
        dfs(cur1.left, cur2.left, cur1, 'l')
        dfs(cur1.right, cur2.right, cur1, 'r')

    dfs(root1, root2, None, None)
    return root1
