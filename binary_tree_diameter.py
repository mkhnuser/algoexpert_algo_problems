class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_height(node):
    if node is None:
        return -1

    left_subtree_height = find_height(node.left)
    right_subtree_height = find_height(node.right)
    return max(left_subtree_height, right_subtree_height) + 1


# NOTE: The solution is inefficient since it invokes height finding at each level.
def recurse_binary_tree_diameter(node):
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 0

    current_level_diameter = (
        (find_height(node.left) if node.left is not None else 0)
        + (find_height(node.right) if node.right is not None else 0)
        + (2 if node.right is not None and node.left is not None else 1)
    )
    left_subtree_diameter = recurse_binary_tree_diameter(node.left)
    right_subtree_diamter = recurse_binary_tree_diameter(node.right)

    return max(current_level_diameter, left_subtree_diameter, right_subtree_diamter)


def binaryTreeDiameter(tree):
    root = tree
    return recurse_binary_tree_diameter(root)


def test_one():
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


def test_two():
    root = BinaryTree(1)
    two = BinaryTree(2)

    root.left = two
    print(binaryTreeDiameter(root))


if __name__ == "__main__":
    test_one()
    test_two()
