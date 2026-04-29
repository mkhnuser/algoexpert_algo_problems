# TODO: Resolve the problem: eliminate the edge cases somehow.
def minHeightBst(array):
    return recurse_solution(array)


def recurse_solution(array):
    root_index = len(array) // 2
    root_value = array[root_index]
    root = BST(root_value)
    further_recurse_solution(node=root, middle_index=root_index, array=array)
    return root


def further_recurse_solution(node, middle_index, array):
    if node is None or len(array) == 0:
        return None

    left_subarray = array[0:middle_index]
    right_subarray = array[middle_index + 1 :]
    left_middle_index = len(left_subarray) // 2
    right_middle_index = len(right_subarray) // 2
    right_middle_value = None
    left_middle_value = None
    if left_subarray:
        left_middle_value = left_subarray[left_middle_index]
    if right_subarray:
        right_middle_value = right_subarray[right_middle_index]

    node.left = further_recurse_solution(
        BST(left_middle_value) if left_middle_value is not None else None,
        left_middle_index,
        left_subarray,
    )
    node.right = further_recurse_solution(
        BST(right_middle_value) if right_middle_value is not None else None,
        right_middle_index,
        right_subarray,
    )
    return node


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
