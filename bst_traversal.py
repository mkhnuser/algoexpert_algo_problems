def inOrderTraverse(tree, array):
    recurse_in_order(tree, array)
    return array


def recurse_in_order(tree, array):
    if tree is not None:
        recurse_in_order(tree.left, array)
        array.append(tree.value)
        recurse_in_order(tree.right, array)


def preOrderTraverse(tree, array):
    recurse_pre_order(tree, array)
    return array


def recurse_pre_order(tree, array):
    array.append(tree.value)

    for child in (tree.left, tree.right):
        if child is None:
            continue
        recurse_pre_order(child, array)


def postOrderTraverse(tree, array):
    recurse_post_order(tree, array)
    return array


def recurse_post_order(tree, array):
    for child in (tree.left, tree.right):
        if child is None:
            continue
        recurse_post_order(child, array)

    array.append(tree.value)
