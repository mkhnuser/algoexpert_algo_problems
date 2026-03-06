def findClosestValueInBst(tree, target):
    return find_node_by_its_value_keeping_closest_value(tree, target, float("+inf"))


def find_node_by_its_value_keeping_closest_value(current_node, value, closest):
    # NOTE: Bases.
    if current_node is None:
        return closest
    if current_node.value == value:
        return current_node.value

    # NOTE: Keep global min.
    current_value = current_node.value
    current_diff = abs(current_value - value)
    closest_diff = abs(closest - value)
    if current_diff < closest_diff:
        closest = current_value

    # NOTE: Recursive cases.
    if current_node.value > value:
        return find_node_by_its_value_keeping_closest_value(
            current_node.left,
            value,
            closest,
        )
    return find_node_by_its_value_keeping_closest_value(
        current_node.right,
        value,
        closest,
    )


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def test():
    root = BST(10)
    n1 = BST(5)
    n2 = BST(15)
    n3 = BST(2)
    n4 = BST(5)
    n5 = BST(13)
    n6 = BST(22)
    n7 = BST(1)
    n8 = BST(14)

    root.left = n1
    root.right = n2

    n1.left = n3
    n1.right = n4

    n2.left = n5
    n2.right = n6

    n3.left = n7

    n5.right = n8

    print(findClosestValueInBst(root, 12))


if __name__ == "__main__":
    test()


########################################################################################
# NOTE: Your assumption that a parent of a given node is the closes value is incorrect.
# Instead, you should compute the abs and keep the global minimum.
#
# def findClosestValueInBst(tree, target):
#     parent_node, found_node = find_node_and_its_parent(None, tree, target)
#
#     if found_node is not None:
#         return found_node.value
#
#     if parent_node is None:
#         raise RuntimeError("Your assumption is incorrect!")
#
#     # NOTE: found_node is None.
#     return parent_node.value
#
#
# def find_node_and_its_parent(parent_node, current_node, value):
#     if current_node is None:
#         return parent_node, None
#
#     if current_node.value == value:
#         return parent_node, current_node
#
#     if current_node.value < value:
#         return find_node_and_its_parent(current_node, current_node.right, value)
#
#     # NOTE: current_node.value > value.
#     return find_node_and_its_parent(current_node, current_node.left, value)
#
#
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# def test():
#     root = BST(10)
#     n1 = BST(5)
#     n2 = BST(15)
#     n3 = BST(2)
#     n4 = BST(5)
#     n5 = BST(13)
#     n6 = BST(22)
#     n7 = BST(1)
#     n8 = BST(14)
#
#     root.left = n1
#     root.right = n2
#
#     n1.left = n3
#     n1.right = n4
#
#     n2.left = n5
#     n2.right = n6
#
#     n3.left = n7
#
#     n5.right = n8
#
#     print(findClosestValueInBst(root, 12))
#
#
# if __name__ == "__main__":
#     test()
#
########################################################################################
