# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distanceK(root: TreeNode, target: TreeNode, k: int):
    adj = dict()

    def dfs(node: TreeNode, parent: TreeNode):
        if not node:
            return
        if parent:
            adj[parent].append(node)

        adj[node] = list()
        adj[node].append(parent)
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    ans = []

    def find_k(node: TreeNode, k: int, pre: TreeNode):
        if k == 0:
            ans.append(node.val)
            return
        if k == 1:
            for each in adj[node]:
                if each and each != pre:
                    ans.append(each.val)
            return

        for i in range(len(adj[node])):
            cur_node = adj[node][i]
            if cur_node and cur_node != pre:
                find_k(cur_node, k - 1, node)

    find_k(target, k, None)

    return ans


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    print(distanceK(root, root.left, 2))
