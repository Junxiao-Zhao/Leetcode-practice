# https://leetcode.com/problems/delete-node-in-a-bst/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def deleteNode(root: TreeNode, key: int):
    if root is None:
        return None
    elif root.val == key:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

    def find_key(node: TreeNode, parent: TreeNode):
        if node is None:
            return
        if node.val == key:
            if not node.left and not node.right:
                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None
            elif node.left and node.right:
                min_node = node.right
                parent = node
                while min_node.left:
                    parent = min_node
                    min_node = min_node.left
                node.val = min_node.val
                new_node = deleteNode(min_node, min_node.val)
                if min_node == parent.left:
                    parent.left = new_node
                else:
                    parent.right = new_node
            elif node.left:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
            else:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right

            return
        elif node.val > key:
            find_key(node.left, node)
        else:
            find_key(node.right, node)

    find_key(root, None)
    return root


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(10)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(15)
    root.right.right.left.left = TreeNode(7)

    deleteNode(root, 5)
