class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_min(node):
    while node.left is not None:
        node = node.left
    return node


def recurse_find_successor(node, node_in_question):
    if node_in_question.right is not None:
        return find_min(node_in_question.right)

    y = node_in_question.parent
    while y is not None and node_in_question != y.left:
        node_in_question = y
        y = y.parent
    return y


def findSuccessor(tree, node):
    root = tree
    node_in_question = node
    return recurse_find_successor(root, node_in_question)
