# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode):

    def DLR(node: TreeNode, pre_node: TreeNode):
        if not node:
            return pre_node
        left = node.left
        right = node.right
        node.left = None
        node.right = None
        if pre_node:
            pre_node.right = node

        node = DLR(left, node)
        node = DLR(right, node)
        return node

    DLR(root, None)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    flatten(root)
