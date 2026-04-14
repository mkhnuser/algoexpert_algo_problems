class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def lmr(node, order):
    if node is None:
        return None

    lmr(node.left, order)
    if node.left is None and node.right is None:
        order.append(node.value)
    lmr(node.right, order)


def compareLeafTraversal(tree1, tree2):
    one_order = []
    two_order = []
    lmr(tree1, one_order)
    lmr(tree2, two_order)
    return one_order == two_order


def test():
    tree1 = BinaryTree(1)
    tree1.left = BinaryTree(2)
    tree1.right = BinaryTree(3)
    tree1.left.left = BinaryTree(4)
    tree1.left.right = BinaryTree(5)
    tree1.right.right = BinaryTree(6)
    tree1.left.right.left = BinaryTree(7)
    tree1.left.right.right = BinaryTree(8)

    tree2 = BinaryTree(1)
    tree2.left = BinaryTree(2)
    tree2.right = BinaryTree(3)
    tree2.left.left = BinaryTree(4)
    tree2.left.right = BinaryTree(7)
    tree2.right.right = BinaryTree(5)
    tree2.right.right.left = BinaryTree(8)
    tree2.right.right.right = BinaryTree(6)
    print(compareLeafTraversal(tree1, tree2))


if __name__ == "__main__":
    test()
