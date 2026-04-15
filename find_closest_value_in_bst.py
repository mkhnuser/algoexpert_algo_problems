# NOTE: The first solution: just construct lmr order and traverse this order to find the closest value.
# def lmr(node, order):
#     if node is None:
#         return
#
#     lmr(node.left, order)
#     order.append(node.value)
#     lmr(node.right, order)
#
#
# def recurse_find_closest_value_in_bst(root, target):
#     lmr_order = []
#     lmr(root, lmr_order)
#     closest = lmr_order[0]
#
#     for i in range(1, len(lmr_order)):
#         value = lmr_order[i]
#         if abs(value - target) < abs(target - closest):
#             closest = value
#
#     return closest
#
#
# def findClosestValueInBst(tree, target):
#     root = tree
#     return recurse_find_closest_value_in_bst(root, target)
#
#
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#
# The solution one ends here.

# NOTE: The second solution start here and uses iteration.

#
# def findClosestValueInBst(tree, target):
#     root = tree
#     current_node = root
#     closest_value = root.value
#
#     while current_node is not None:
#         current_distance = abs(current_node.value - target)
#         closest_value = (
#             current_node.value
#             if current_distance < abs(target - closest_value)
#             else closest_value
#         )
#
#         if current_node.value == target:
#             break
#         elif current_node.value > target:
#             current_node = current_node.left
#         else:
#             current_node = current_node.right
#
#     return closest_value
#
#
# class BST:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None


# NOTE: The third solution begins here, mimics the seconds one, but uses recursion.
def recurse_find_closest_value_in_bst(node, target, closest_value):
    if node is None:
        return closest_value

    current_distance = abs(node.value - target)
    distance_so_far = abs(closest_value - target)

    if current_distance < distance_so_far:
        closest_value = node.value

    if node.value == target:
        return closest_value
    elif node.value > target:
        return recurse_find_closest_value_in_bst(node.left, target, closest_value)
    else:
        return recurse_find_closest_value_in_bst(node.right, target, closest_value)


def findClosestValueInBst(tree, target):
    root = tree
    return recurse_find_closest_value_in_bst(tree, target, float("+inf"))


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
