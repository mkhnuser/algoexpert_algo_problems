class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def recurse_insertion(self, current_node, node_to_insert):
        if current_node is None:
            return node_to_insert

        if node_to_insert.value >= current_node.value:
            current_node.right = self.recurse_insertion(
                current_node.right,
                node_to_insert,
            )
        else:
            current_node.left = self.recurse_insertion(
                current_node.left,
                node_to_insert,
            )

        return current_node

    def insert(self, value):
        self.recurse_insertion(self, BST(value))
        return self

    def recurse_contains(self, node, node_to_check):
        if node is None:
            return False
        if node.value == node_to_check.value:
            return True
        if node_to_check.value > node.value:
            return self.recurse_contains(node.right, node_to_check)
        return self.recurse_contains(node.left, node_to_check)

    def contains(self, value):
        return self.recurse_contains(self, BST(value))

    def find_node_and_its_parent_by_value(self, current_node, parent, value):
        if current_node is None:
            return None, None

        if current_node.value == value:
            return parent, current_node

        if value > current_node.value:
            return self.find_node_and_its_parent_by_value(
                current_node=current_node.right,
                parent=current_node,
                value=value,
            )
        return self.find_node_and_its_parent_by_value(
            current_node=current_node.left,
            parent=current_node,
            value=value,
        )

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    def is_the_only_node(self, p, n):
        return p is None and n.left is None and n.right is None

    def remove(self, value, p=None):
        p, n = self.find_node_and_its_parent_by_value(
            current_node=self,
            parent=p,
            value=value,
        )
        if n is None or self.is_the_only_node(p, n):
            return

        if n.left and n.right:
            s = n.right.find_min(n.right)
            n.value = s.value
            n.right.remove(s.value, n)
        elif n.left is None and n.right is None:
            if p.left is n:
                p.left = None
            elif p.right is n:
                p.right = None
        elif n.left:
            pred = n.left.find_max(n.left)
            n.value = pred.value
            n.left.remove(pred.value, n)
        elif n.right:
            s = n.right.find_min(n.right)
            n.value = s.value
            n.right.remove(s.value, n)

        return self
