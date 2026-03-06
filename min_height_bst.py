def minHeightBst(array):
    return recurse_min_height_bst(None, array)


def recurse_min_height_bst(root_value, array):
    if not array:
        return None

    if len(array) == 1:
        return BST(array[0])

    middle = len(array) // 2
    root_value = array[middle]
    root = BST(root_value)

    root.left = recurse_min_height_bst(root_value, array[:middle])
    root.right = recurse_min_height_bst(root_value, array[middle + 1 :])

    return root


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def test():
    test_array = [1, 2, 5, 7, 10, 13, 14, 15, 22]
    root = recurse_min_height_bst(None, test_array)


if __name__ == "__main__":
    test()
