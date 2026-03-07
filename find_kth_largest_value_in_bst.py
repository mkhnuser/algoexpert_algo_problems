class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # NOTE:
    # 1. Calc. in-order traversal.
    # 2. Find kth element from the end of an array.
    array = []
    recurse_in_order(tree, array)
    return array[-k].value


def recurse_in_order(node, array):
    if node is not None:
        recurse_in_order(node.left, array)
        array.append(node)
        recurse_in_order(node.right, array)
