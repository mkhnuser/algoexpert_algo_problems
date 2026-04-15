def inOrderTraverse(tree, array):
    root = tree
    array = []

    def recurse_in(node, array):
        if node is None:
            return
        recurse_in(node.left, array)
        array.append(node.value)
        recurse_in(node.right, array)

    recurse_in(root, array)
    return array


def preOrderTraverse(tree, array):
    root = tree
    array = []

    def recurse_pre(node, array):
        if node is None:
            return
        array.append(node.value)
        recurse_pre(node.left, array)
        recurse_pre(node.right, array)

    recurse_pre(root, array)
    return array


def postOrderTraverse(tree, array):
    root = tree
    array = []

    def recurse_post(node, array):
        if node is None:
            return
        recurse_post(node.left, array)
        recurse_post(node.right, array)
        array.append(node.value)

    recurse_post(root, array)
    return array
