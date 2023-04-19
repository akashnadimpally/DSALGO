class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution(object):
    def printRootToLeaf(self, root: TreeNode):
        if (root is None):
            return []

        arr = []
        self.printRootToLeafImpl(root, arr, 0)

    def printRootToLeafImpl(self, root: TreeNode, arr: list[int], index: int):
        if (root is None):
            return []

        arr[index] = root.value

        if (root.left is None) and (root.right is None):
            self.printArray(arr, index)

        self.printRootToLeafImpl(root.left, arr, index + 1)
        self.printRootToLeafImpl(root.right, arr, index + 1)


    def printArray(self, arr, index):
        for i in range(0, index):
            print(arr[i])

        print("")




