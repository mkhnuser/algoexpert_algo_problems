from typing import cast


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    array = preOrderTraversalValues

    if not array:
        return BST(None)

    root_value = array[0]
    root = BST(root_value)
    left = 1
    right = len(array)
    recurse_reconstruction(root, array, left, right)
    return root


def recurse_reconstruction(root, array, left, right):
    left_child_value = None
    left_child_index = None
    right_child_value = None
    right_child_index = None

    for i in range(left, right):
        potential_child_value = array[i]
        if left_child_value is None and potential_child_value < root.value:
            left_child_value = potential_child_value
            left_child_index = i
        if right_child_value is None and potential_child_value >= root.value:
            right_child_value = potential_child_value
            right_child_index = i

    left_child = BST(left_child_value) if left_child_value is not None else None
    right_child = BST(right_child_value) if right_child_value is not None else None
    root.left = left_child
    root.right = right_child

    if left_child_value is not None and right_child_value is not None:
        # NOTE: Both left and right child have been found.
        left_child_index = cast(int, left_child_index)
        right_child_index = cast(int, right_child_index)
        recurse_reconstruction(
            left_child,
            array,
            left_child_index + 1,
            right_child_index,
        )
        recurse_reconstruction(
            right_child,
            array,
            right_child_index + 1,
            right,
        )
    elif left_child_value is not None:
        left_child_index = cast(int, left_child_index)
        recurse_reconstruction(
            left_child,
            array,
            left_child_index + 1,
            right,
        )
    elif right_child_value is not None:
        right_child_index = cast(int, right_child_index)
        recurse_reconstruction(
            right_child,
            array,
            right_child_index + 1,
            right,
        )


def test():
    array = [10, 4, 2, 1, 5, 17, 19, 18]
    #        0   1  2  3  4  5   6   7
    new_root = reconstructBst(array)
    assert new_root.value == 10
    assert new_root.left.value == 4
    assert new_root.right.value == 17
    assert new_root.left.left.value == 2
    assert new_root.left.left.left.value == 1
    assert new_root.left.right.value == 5
    assert new_root.right.right.value == 19
    assert new_root.right.right.left.value == 18


if __name__ == "__main__":
    test()
