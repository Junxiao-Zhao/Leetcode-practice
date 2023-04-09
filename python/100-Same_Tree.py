# https://leetcode.com/problems/same-tree/


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode):
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False

    stack_p = [p]
    stack_q = [q]
    isSame = True

    while len(stack_p) > 0 and len(stack_q) > 0 and len(stack_p) == len(
            stack_q):
        cur_p = stack_p.pop(0)
        cur_q = stack_q.pop(0)

        if cur_p is None and cur_q is None:
            continue
        elif cur_p is None or cur_q is None:
            isSame = False
            break

        if cur_p.val != cur_q.val:
            isSame = False
            break

        stack_p.append(cur_p.left)
        stack_q.append(cur_q.left)
        stack_p.append(cur_p.right)
        stack_q.append(cur_q.right)

    return isSame


if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = p
    print(isSameTree(p, q))
