OPERATORS = set((-1, -2, -3, -4))


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def recurse_evaluation(node):
    value = node.value

    if value in OPERATORS:
        if value == -1:
            return recurse_evaluation(node.left) + recurse_evaluation(node.right)
        elif value == -2:
            return recurse_evaluation(node.left) - recurse_evaluation(node.right)
        elif value == -3:
            return int(recurse_evaluation(node.left) / recurse_evaluation(node.right))
        elif value == -4:
            return recurse_evaluation(node.left) * recurse_evaluation(node.right)
    else:
        return value


def evaluateExpressionTree(tree):
    root = tree
    return recurse_evaluation(root)


def test():
    root = BinaryTree(-1)
    n1 = BinaryTree(-2)
    n2 = BinaryTree(-4)
    n3 = BinaryTree(2)
    n4 = BinaryTree(3)
    n5 = BinaryTree(2)
    n6 = BinaryTree(-3)
    n7 = BinaryTree(8)
    n8 = BinaryTree(3)

    root.left = n1
    root.right = n6

    n1.left = n2
    n1.right = n5

    n2.left = n3
    n2.right = n4

    n6.left = n7
    n6.right = n8

    print(evaluateExpressionTree(root))


if __name__ == "__main__":
    test()
