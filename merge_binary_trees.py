class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def initialize_empty_nodes(node1, node2):
    # NOTE: Terminate recursion.
    if node1 is None and node2 is None:
        return

    # NOTE: Consider left children cases.
    if node1.left is not None and node2.left is None:
        node2.left = BinaryTree(0)
    if node1.left is None and node2.left is not None:
        node1.left = BinaryTree(0)

    # NOTE: Consider right children cases.
    if node1.right is not None and node2.right is None:
        node2.right = BinaryTree(0)
    if node1.right is None and node2.right is not None:
        node1.right = BinaryTree(0)

    # NOTE: Recurse.
    initialize_empty_nodes(node1.left, node2.left)
    initialize_empty_nodes(node1.right, node2.right)


def sum_up_the_values_respectively(result_node, node1, node2):
    # NOTE: Terminate recursion.
    if node1 is None and node2 is None:
        return

    result_node.value = node1.value + node2.value
    left_child = (
        BinaryTree(0) if (node1.left is not None and node2.left is not None) else None
    )
    right_child = (
        BinaryTree(0) if (node1.right is not None and node2.right is not None) else None
    )
    result_node.left = left_child
    result_node.right = right_child

    # NOTE: Recurse.
    sum_up_the_values_respectively(left_child, node1.left, node2.left)
    sum_up_the_values_respectively(right_child, node1.right, node2.right)


def mergeBinaryTrees(tree1, tree2):
    # NOTE:
    # 1. Create empty nodes with zero values to have the same tree structure;
    # 2. Iterate over both trees and sum the values of respective nodes.
    root1 = tree1
    root2 = tree2
    initialize_empty_nodes(root1, root2)
    new_root = BinaryTree(0)
    sum_up_the_values_respectively(new_root, root1, root2)
    return new_root


def test():
    tree1 = BinaryTree(1)
    tree1.left = BinaryTree(3)
    tree1.left.left = BinaryTree(7)
    tree1.left.right = BinaryTree(4)
    tree1.right = BinaryTree(2)

    tree2 = BinaryTree(1)
    tree2.left = BinaryTree(5)
    tree2.left.left = BinaryTree(2)
    tree2.right = BinaryTree(9)
    tree2.right.left = BinaryTree(7)
    tree2.right.right = BinaryTree(6)
    new_tree = mergeBinaryTrees(tree1, tree2)
    breakpoint()


if __name__ == "__main__":
    test()
