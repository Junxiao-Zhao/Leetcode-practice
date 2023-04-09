# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root: TreeNode):
    if not root:
        return []

    l1 = [root]
    l2 = []
    ans = [[root.val]]

    need_reverse = True
    while len(l1) > 0:

        cur = l1.pop(0)
        if cur.left:
            l2.append(cur.left)
        if cur.right:
            l2.append(cur.right)

        if len(l1) == 0:
            l1, l2 = l2, l1
            row_val = [
                each.val
                for each in (l1 if not need_reverse else list(reversed(l1)))
            ]
            if len(row_val) > 0:
                ans.append(row_val)
            need_reverse = not need_reverse

    return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(zigzagLevelOrder(root))
