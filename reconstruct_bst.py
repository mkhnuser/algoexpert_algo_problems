class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def recurse_reconstruction(array):
    if not array:
        return None

    root_value = array[0]
    root = BST(root_value)

    # NOTE: Find the first greater than or equal to value (if any).
    right_start = len(array)
    for i in range(1, len(array)):
        if array[i] >= root_value:
            right_start = i
            break

    left_subtree = array[1:right_start]
    right_subtree = array[right_start:]

    root.left = recurse_reconstruction(left_subtree)
    root.right = recurse_reconstruction(right_subtree)

    return root


def reconstructBst(preOrderTraversalValues):
    array = preOrderTraversalValues
    return recurse_reconstruction(array)


def test():
    preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]
    reconstructBst(preOrderTraversalValues)


if __name__ == "__main__":
    test()
