# https://leetcode.com/problems/find-mode-in-binary-search-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMode(root: TreeNode):
    count = dict()

    def dfs(node: TreeNode):
        if not node:
            return

        count.setdefault(node.val, 0)
        count[node.val] += 1
        dfs(node.left)
        dfs(node.right)

    dfs(root)

    items = list(count.items())
    items.sort(key=lambda x: x[1], reverse=True)

    ans = []
    most = items[0][1]
    for val, num in items:
        if num < most:
            break
        ans.append(val)

    return ans
