class BST:
    # NOTE: We hack our way to satisfy a rather strange requirement that
    # We can't delete a node in a BST if it's the only node (if it's root and no other nodes are present).
    bst_size = 1

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = BST(value)
        self.recurse_insertion(self, node)
        self.bst_size += 1
        return self

    def recurse_insertion(self, current_node, node):
        if current_node.value <= node.value:
            # NOTE: Go right.
            if current_node.right is None:
                current_node.right = node
            else:
                self.recurse_insertion(current_node.right, node)
        else:
            # NOTE: Go left.
            if current_node.left is None:
                current_node.left = node
            else:
                self.recurse_insertion(current_node.left, node)

    def contains(self, value):
        node = BST(value)
        return self.recurse_contains(self, node)

    def recurse_contains(self, current_node, node):
        if current_node is None:
            return False
        if current_node.value == node.value:
            return True

        if current_node.value < node.value:
            # NOTE: Search right.
            return self.recurse_contains(current_node.right, node)
        else:
            # NOTE: Search left.
            return self.recurse_contains(current_node.left, node)

    def remove(self, value):
        if self.bst_size <= 1:
            # NOTE: If there is only one node in the tree, don't remove it!
            return

        p_d, d = self.find_node_and_its_parent_by_value(None, self, value)

        if d is None:
            # NOTE: We haven't found a node to be deleted, so just terminate this procedure.
            return

        new_node = self.remove_node(p_d, d)
        self.bst_size -= 1
        return new_node

    def remove_node(self, p_d, d):
        if d.left is None:
            # NOTE: Transplant d with its right child (if any).
            self.transplant(p_d, d, d, d.right)
            return d.right
        elif d.right is None:
            # NOTE: Transplant d with its left child (if any).
            self.transplant(p_d, d, d, d.left)
            return d.left
        else:
            # NOTE: d has both the left child and the right child.
            # Therefore, we have to transplant d with either its successor or predecessor.
            #
            # Suppose succ is the successor of d.
            # Consider two cases: succ is the direct right child of d,
            # and succ is not the direct right child of d.
            #
            # If succ is the direct child, just transplant the whole branch of the tree.
            # Otherwise, transplant succ with its right child and only then transplant d with succ.
            #
            # Overall, make sure to update all the references.
            p_s, succ = self.find_minimum_and_its_parent(d, d.right)

            if succ != d.right:
                # NOTE: Make sure to transplant the right child of a successor (if any).
                self.transplant(p_s, succ, succ, succ.right)
                succ.right = d.right

            self.transplant(p_d, d, d, succ)
            succ.left = d.left
            return succ

    def transplant(self, p1, n1, p2, n2):
        # NOTE: Transplant n1 with n2.
        # p1 is the parent of n1, p2 is the parent of n2.
        if p1 is None:
            pass
        elif n1 == p1.left:
            p1.left = n2
        else:
            p1.right = n2

        if n2 is not None:
            pass

    def find_minimum_and_its_parent(self, parent, node):
        while node.left is not None:
            parent = node
            node = node.left
        return parent, node

    def find_node_and_its_parent_by_value(self, parent_node, current_node, value):
        if current_node is None:
            return parent_node, None

        if current_node.value == value:
            return parent_node, current_node

        if current_node.value < value:
            return self.find_node_and_its_parent_by_value(
                current_node,
                current_node.right,
                value,
            )
        return self.find_node_and_its_parent_by_value(
            current_node,
            current_node.left,
            value,
        )


def test():
    root = BST(10)
    for value in (5, 15, 2, 5, 13, 22, 1, 12, 14):
        root.insert(value)
    breakpoint()


if __name__ == "__main__":
    test()
