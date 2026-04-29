class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def do_in_order(node, order):
    if node is None:
        return
    do_in_order(node.left, order)
    order.append(node.value)
    do_in_order(node.right, order)


def findKthLargestValueInBst(tree, k):
    # NOTE: O(n) time, O(n) space.
    order = []
    do_in_order(tree, order)
    return order[-k]
