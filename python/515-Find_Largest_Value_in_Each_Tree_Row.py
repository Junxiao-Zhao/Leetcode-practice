# https://leetcode.com/problems/find-largest-value-in-each-tree-row/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def largestValues(root: TreeNode):
    if not root:
        return []

    l1 = [root]
    l2 = []
    row_max = float("-inf")
    ans = []

    while len(l1) > 0:

        cur = l1.pop(0)
        if cur.left:
            l2.append(cur.left)
        if cur.right:
            l2.append(cur.right)

        if cur.val > row_max:
            row_max = cur.val

        if len(l1) == 0:
            l1, l2 = l2, l1
            ans.append(row_max)
            row_max = float("-inf")

    return ans
