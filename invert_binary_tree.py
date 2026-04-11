# NOTE: A recursive solution.


def swap(parent, left_child, right_child):
    parent.left = right_child
    parent.right = left_child


def recurse_binary_tree_inversion(node):
    if node is None:
        return

    swap(node, node.left, node.right)
    recurse_binary_tree_inversion(node.left)
    recurse_binary_tree_inversion(node.right)


def invertBinaryTree(tree):
    root = tree
    return recurse_binary_tree_inversion(root)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# NOTE: An iterative approach.
from queue import Queue


def invertBinaryTree(tree):
    root = tree
    q = Queue()
    q.put(root)

    while q.qsize() > 0:
        item = q.get()

        left_child = item.left
        right_child = item.right

        item.left = right_child
        item.right = left_child

        if right_child is not None:
            q.put(right_child)
        if left_child is not None:
            q.put(left_child)

        q.task_done()


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def test_one():
    root = BinaryTree(1)

    node_2 = BinaryTree(2)
    node_3 = BinaryTree(3)

    node_4 = BinaryTree(4)
    node_5 = BinaryTree(5)
    node_6 = BinaryTree(6)
    node_7 = BinaryTree(7)

    node_8 = BinaryTree(8)
    node_9 = BinaryTree(9)

    root.left = node_2
    root.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    node_4.left = node_8
    node_4.right = node_9

    invertBinaryTree(root)
    breakpoint()


def test_two():
    root = BinaryTree(1)
    node_2 = BinaryTree(2)
    root.left = node_2
    invertBinaryTree(root)
    breakpoint()


if __name__ == "__main__":
    test_one()
    test_two()
