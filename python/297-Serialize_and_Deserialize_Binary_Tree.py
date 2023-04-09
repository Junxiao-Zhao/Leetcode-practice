# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        ans = ""

        def dfs(node: TreeNode):
            nonlocal ans
            if not node:
                ans += ","
                return
            ans += str(node.val) + ","
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        data = data.split(",")

        def build_tree(data_list):
            if len(data_list) == 0 or data_list[0] == "":
                data_list.pop(0)
                return None

            node = TreeNode(int(data_list.pop(0)))
            node.left = build_tree(data_list)
            node.right = build_tree(data_list)
            return node

        return build_tree(data)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    ser = Codec()
    a = ser.serialize(root)
    print(a)
    # b = ser.deserialize(a)
