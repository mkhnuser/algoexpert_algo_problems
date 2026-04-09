class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return recurse_binary_tree_diameter(tree)[-1]


def recurse_binary_tree_diameter(node):
    if node is None:
        # NOTE: Return height, diameter at the same time.
        return -1, 0

    left_height, left_diameter = recurse_binary_tree_diameter(node.left)
    right_height, right_diameter = recurse_binary_tree_diameter(node.right)

    height = max(left_height, right_height) + 1
    diameter_through_node = left_height + right_height + 2
    diameter = max(diameter_through_node, left_diameter, right_diameter)

    return height, diameter


def test():
    root = BinaryTree(1)

    two = BinaryTree(2)
    three = BinaryTree(3)

    root.left = three
    root.right = two

    seven = BinaryTree(7)
    four = BinaryTree(4)

    three.left = seven
    three.right = four

    eight = BinaryTree(8)
    five = BinaryTree(5)

    seven.left = eight
    four.right = five

    nine = BinaryTree(9)
    six = BinaryTree(6)

    eight.left = nine
    five.right = six

    print(binaryTreeDiameter(root))


if __name__ == "__main__":
    test()
