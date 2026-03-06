def nodeDepths(root):
    depth = 0
    return recurse_node_depths(root, depth)


def recurse_node_depths(node, depth):
    if not node:
        return 0

    left_sum = recurse_node_depths(node.left, depth + 1)
    right_sum = recurse_node_depths(node.right, depth + 1)
    return depth + left_sum + right_sum


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
    pass
