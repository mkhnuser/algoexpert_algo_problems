OPERATORS = set((-1, -2, -3, -4))


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    return recurse_evaluate_expression_tree(tree)


def recurse_evaluate_expression_tree(node):
    if node.value not in OPERATORS:
        value = node.value
        return value

    op = node.value
    if op == -1:
        return recurse_evaluate_expression_tree(
            node.left
        ) + recurse_evaluate_expression_tree(node.right)
    elif op == -2:
        return recurse_evaluate_expression_tree(
            node.left
        ) - recurse_evaluate_expression_tree(node.right)
    elif op == -3:
        return int(
            recurse_evaluate_expression_tree(node.left)
            / recurse_evaluate_expression_tree(node.right)
        )
    elif op == -4:
        return recurse_evaluate_expression_tree(
            node.left
        ) * recurse_evaluate_expression_tree(node.right)
    else:
        raise RuntimeError("Invalid Operator!")


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
