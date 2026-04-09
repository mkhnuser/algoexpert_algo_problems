from queue import Queue


def invertBinaryTree(tree):
    return invert_recursively(tree, tree.left, tree.right)


def invert_recursively(parent, left, right):
    if left is None and right is None:
        return

    parent.left = right
    parent.right = left

    if left is not None:
        invert_recursively(left, left.left, left.right)
    if right is not None:
        invert_recursively(right, right.left, right.right)


def swap(u_p, u, v_p, v):
    if u_p.left is u:
        u_p.left = v
        u_p.right = u
    else:
        u_p.right = v
        u_p.left = u


def invert_bfs(tree):
    q = Queue()
    q.put(tree)

    while q.qsize() > 0:
        v = q.get()

        if v is None:
            continue

        left_child = v.left
        right_child = v.right

        q.put(left_child)
        q.put(right_child)

        swap(v, left_child, v, right_child)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def test():
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
    test_two()
