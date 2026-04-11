def recurse_node_depths(node, depth):
    if node is None:
        return 0

    left_depth_summation = recurse_node_depths(node.left, depth=depth + 1)
    right_depth_summation = recurse_node_depths(node.right, depth=depth + 1)
    return depth + left_depth_summation + right_depth_summation


def nodeDepths(root):
    # NOTE: The depth of the root is 0.
    # The depth of the first "layer" is 1, and so on.
    return recurse_node_depths(root, 0)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def test():
    root = BinaryTree(1)
    two = BinaryTree(2)
    three = BinaryTree(3)
    four = BinaryTree(4)
    five = BinaryTree(5)
    six = BinaryTree(6)
    seven = BinaryTree(7)
    eight = BinaryTree(8)
    nine = BinaryTree(9)
    # ten = BinaryTree(10)

    root.left = two
    root.right = three

    two.left = four
    two.right = five

    four.left = eight
    four.right = nine

    # five.left = ten

    three.left = six
    three.right = seven

    print(nodeDepths(root))


if __name__ == "__main__":
    test()
