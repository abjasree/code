# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    if root == None:
        return 0
    current_sum = 0
    sums = []
    helper(root, current_sum, sums)
    return sums


def helper(tree, current_sum, sums):
    current_sum = current_sum + tree.value
    if tree.right == None and tree.left == None:
        sums.append(current_sum)
    elif tree.right == None:
        helper(tree.left, current_sum, sums)
    elif tree.left == None:
        helper(tree.right, current_sum, sums)
    else:
        helper(tree.left, current_sum, sums)
        helper(tree.right, current_sum, sums)
