# https://leetcode.com/problems/binary-tree-right-side-view/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root: TreeNode):
    if not root:
        return []

    l1 = [root]
    l2 = []
    ans = [root.val]

    while len(l1) > 0:

        cur = l1.pop(0)
        if cur.left:
            l2.append(cur.left)
        if cur.right:
            l2.append(cur.right)

        if len(l1) == 0:
            l1, l2 = l2, l1
            if len(l1) > 0:
                ans.append(l1[-1].val)

    return ans
