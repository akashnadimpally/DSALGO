
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None


class Solution(object):
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

        # if root is None:
        #     return []
        # output, stack = [], [root]
        # while stack:
        #     root = stack.pop()
        #     if root is not None:
        #         output.append(root.val)
        #         if root.right is not None:
        #             stack.append(root.right)
        #         if root.left is not None:
        #             stack.append(root.left)
        #
        # return output



