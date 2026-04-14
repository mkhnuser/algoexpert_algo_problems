from queue import Queue


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sum_binary_tree(node):
    summation = 0
    q = Queue()
    q.put(node)

    while q.qsize() > 0:
        current = q.get()
        summation += current.value

        if current.left is not None:
            q.put(current.left)
        if current.right is not None:
            q.put(current.right)

    return summation


def solve_tree(node):
    if node is None:
        return 0

    node.summation = node.value + solve_tree(node.left) + solve_tree(node.right)
    return node.summation


def does_a_subtree_exist(node, half_root_summation):
    if node is None:
        return False

    if node.summation == half_root_summation:
        return True

    return does_a_subtree_exist(
        node.left,
        half_root_summation,
    ) or does_a_subtree_exist(
        node.right,
        half_root_summation,
    )


def splitBinaryTree(tree):
    root = tree
    solve_tree(root)

    if root.summation % 2 != 0:
        return 0

    half_root_summation = root.summation / 2
    if does_a_subtree_exist(root, half_root_summation):
        return int(half_root_summation)
    return 0


def test():
    tree = BinaryTree(2)
    tree.left = BinaryTree(4)
    tree.left.left = BinaryTree(4)
    tree.left.right = BinaryTree(6)
    tree.right = BinaryTree(10)
    tree.right.left = BinaryTree(3)
    tree.right.right = BinaryTree(3)
    solve_tree(tree)
    breakpoint()


if __name__ == "__main__":
    test()
