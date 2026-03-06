class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return recurse_validate_bst(
        node=tree,
        lower_bound=float("-inf"),
        upper_bound=float("+inf"),
    )


def recurse_validate_bst(node, lower_bound, upper_bound):
    if node is None:
        return True

    # NOTE: A normal condition: left < node.value <= right.
    if node.value >= upper_bound or node.value < lower_bound:
        return False

    return recurse_validate_bst(
        node.left,
        lower_bound=lower_bound,
        upper_bound=node.value,
    ) and recurse_validate_bst(
        node.right,
        lower_bound=node.value,
        upper_bound=upper_bound,
    )
