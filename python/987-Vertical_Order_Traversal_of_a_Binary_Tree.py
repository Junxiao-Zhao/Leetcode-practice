# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root: TreeNode):
    ans = dict()

    cur_row = [[root, 0]]
    next_row = []
    row_values = dict()

    while len(cur_row) > 0:
        node, v = cur_row.pop(0)
        if node.left:
            next_row.append([node.left, v - 1])
        if node.right:
            next_row.append([node.right, v + 1])

        row_values.setdefault(v, [])
        row_values[v].append(node.val)

        if len(cur_row) == 0:
            cur_row, next_row = next_row, cur_row
            for key in row_values.keys():
                row_values[key].sort()
                ans.setdefault(key, [])
                ans[key] += row_values[key]
            row_values = dict()

    ans = dict(sorted(ans.items(), key=lambda x: x[0]))

    return list(ans.values())
