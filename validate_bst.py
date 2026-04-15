class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def recurse_validation(node, lower_bound, upper_bound):
    if node is None:
        return True

    return (
        (node.value >= lower_bound and node.value < upper_bound)
        and recurse_validation(
            node.left,
            lower_bound=lower_bound,
            upper_bound=node.value,
        )
        and recurse_validation(
            node.right,
            lower_bound=node.value,
            upper_bound=upper_bound,
        )
    )


def validateBst(tree):
    root = tree
    return recurse_validation(
        node=root,
        lower_bound=float("-inf"),
        upper_bound=float("+inf"),
    )
