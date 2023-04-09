# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode):

    ans = None

    def dfs(node: TreeNode):
        if not node:
            return False
        lson = dfs(node.left)
        rson = dfs(node.right)
        nonlocal ans
        if (lson and rson) or ((node.val == p.val or node.val == q.val) and
                               (lson or rson)):
            ans = node

        return lson or rson or (node.val == p.val or node.val == q.val)

    dfs(root)
    return ans
