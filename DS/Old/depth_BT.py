import math


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


def max_depth(root: TreeNode) -> int:
    if (root == None):
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1