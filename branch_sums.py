class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    output = []
    starting_sum = 0
    recurse_branch_sums(root, starting_sum, output)
    return output


def recurse_branch_sums(node, current_sum, output):
    current_sum += node.value

    if node.left is None and node.right is None:
        output.append(current_sum)
        return

    if node.left:
        recurse_branch_sums(node.left, current_sum, output)
    if node.right:
        recurse_branch_sums(node.right, current_sum, output)


def test():
    root = BinaryTree(1)
    two = BinaryTree(2)
    three = BinaryTree(3)
    four = BinaryTree(4)
    five = BinaryTree(5)
    six = BinaryTree(6)
    seven = BinaryTree(7)
    eight = BinaryTree(8)
    nine = BinaryTree(9)
    ten = BinaryTree(10)

    root.left = two
    root.right = three

    two.left = four
    two.right = five

    four.left = eight
    four.right = nine

    five.left = ten

    three.left = six
    three.right = seven

    print(branchSums(root))


if __name__ == "__main__":
    test()
