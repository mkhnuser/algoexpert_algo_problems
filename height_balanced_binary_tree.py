# NOTE: The solution is inefficient because it invokes height function at each node.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_height(node):
    if node is None:
        return -1

    l = find_height(node.left)
    r = find_height(node.right)
    return max(l, r) + 1


def recurse_height_balanced_binary_tree(node):
    if node is None:
        return True

    l = find_height(node.left)
    r = find_height(node.right)

    if abs(l - r) > 1:
        return False

    return recurse_height_balanced_binary_tree(
        node.left,
    ) and recurse_height_balanced_binary_tree(
        node.right,
    )


def heightBalancedBinaryTree(tree):
    root = tree
    return recurse_height_balanced_binary_tree(root)
