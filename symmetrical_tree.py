# NOTE: LMR, RML solution.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lmr(node, lmr_order):
    if node is not None:
        lmr(node.left, lmr_order)
        lmr_order.append(node.value)
        lmr(node.right, lmr_order)


def rml(node, rml_order):
    if node is not None:
        rml(node.right, rml_order)
        rml_order.append(node.value)
        rml(node.left, rml_order)


def symmetricalTree(tree):
    root = tree
    lmr_order = []
    rml_order = []
    lmr(root, lmr_order)
    rml(root, rml_order)
    return lmr_order == rml_order


# NOTE: BFS Solution.
from queue import Queue


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    if tree is None:
        return True

    root = tree

    q = Queue()
    q.put((root.left, root.right))

    while q.qsize() > 0:
        n1, n2 = q.get()

        if n1 is None and n2 is None:
            continue
        if n1 is None and n2 is not None:
            return False
        if n1 is not None and n2 is None:
            return False

        if n1.value != n2.value:
            return False

        q.put((n1.left, n2.right))
        q.put((n1.right, n2.left))

    return True
