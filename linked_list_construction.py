class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        prev_head = self.head

        if prev_head is None:
            self.head = node
            return

        prev_item = node.prev
        next_item = node.next

        if prev_item is not None:
            prev_item.next = next_item
        if next_item is not None:
            next_item.prev = prev_item

        node.prev = None
        self.head = node
        node.next = prev_head
        prev_head.prev = node

    def getHead(self):
        return self.head

    def setTail(self, node):
        prev_tail = self.tail

        if prev_tail is None:
            self.tail = node
            return

        prev_item = node.prev
        next_item = node.next

        if prev_item is not None:
            prev_item.next = next_item
        if next_item is not None:
            next_item.prev = prev_item

        node.next = None
        self.tail = node
        node.prev = prev_tail
        prev_tail.next = node

    def getTail(self):
        return self.tail

    def insertBefore(self, node, nodeToInsert):
        nodeToInsert_prev = nodeToInsert.prev
        nodeToInsert_next = nodeToInsert.next

        if nodeToInsert_prev is not None:
            nodeToInsert_prev.next = nodeToInsert_next
        if nodeToInsert_next is not None:
            nodeToInsert_next.prev = nodeToInsert_prev

        nodeToInsert.next = None
        nodeToInsert.prev = None

        prev_item = node.prev

        if prev_item is not None:
            prev_item.next = nodeToInsert
            nodeToInsert.prev = prev_item
        if prev_item is None:
            self.head = nodeToInsert

        node.prev = nodeToInsert
        nodeToInsert.next = node

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert_prev = nodeToInsert.prev
        nodeToInsert_next = nodeToInsert.next

        if nodeToInsert_prev is not None:
            nodeToInsert_prev.next = nodeToInsert_next
        if nodeToInsert_next is not None:
            nodeToInsert_next.prev = nodeToInsert_prev

        nodeToInsert.next = None
        nodeToInsert.prev = None

        next_item = node.next

        if next_item is not None:
            next_item.prev = nodeToInsert
            nodeToInsert.next = next_item
        if next_item is None:
            self.tail = nodeToInsert

        node.next = nodeToInsert
        nodeToInsert.prev = node

    def insertAtPosition(self, position, nodeToInsert):
        # WARNING: WE START COUNTING AT ONE.

        nodeToInsert.next = None
        nodeToInsert.prev = None

        if position == 1:
            prev_head = self.head
            self.head = nodeToInsert
            nodeToInsert.next = prev_head
            prev_head.prev = nodeToInsert
            return

        assert position >= 2
        position -= 2

        head = self.head
        while head and position > 0:
            head = head.next
            position -= 1

        if head is None:
            raise Exception("Index out of bound!")

        next_item = head.next
        nodeToInsert.next = next_item
        nodeToInsert.prev = head
        head.next = nodeToInsert

        if next_item is not None:
            next_item.prev = nodeToInsert
        else:
            self.tail = nodeToInsert

    def removeNodesWithValue(self, value):
        head = self.head

        while head is not None:
            current_value = head.value
            prev_item = head.prev
            next_item = head.next

            if current_value == value:
                self.doubly_connect(prev_item, next_item)

            head = head.next

    def remove(self, node):
        head = self.head

        while head is not None:
            prev_item = head.prev
            next_item = head.next

            if head is node:
                self.doubly_connect(prev_item, next_item)

            head = head.next

    def doubly_connect(self, prev_item, next_item):
        if prev_item is not None:
            prev_item.next = next_item
        else:
            if next_item is not None:
                next_item.prev = prev_item
                self.head = next_item
            else:
                # NOTE: prev_item is None and next_item is None, so we've deleted the only node in our list.
                self.head = None

        if next_item is not None:
            next_item.prev = prev_item
        else:
            if prev_item is not None:
                prev_item.next = next_item
                self.tail = prev_item
            else:
                # NOTE: prev_item is None and next_item is None, so we've deleted the only node in our list.
                self.tail = None

    def containsNodeWithValue(self, value):
        head = self.head

        while head is not None:
            if head.value == value:
                return True
            head = head.next

        return False

    def printList(self):
        head = self.head

        while head is not None:
            print(
                f"{head.prev.value if head.prev is not None else head.prev} <-> {head.value} <-> {head.next.value if head.next is not None else head.next}"
            )
            head = head.next


def test_one():
    one = Node(1)
    two = Node(2)
    three = Node(3)

    one.next = two
    two.prev = one
    two.next = three
    three.prev = two

    list_ = DoublyLinkedList()
    list_.setHead(one)
    list_.setTail(three)

    assert list_.containsNodeWithValue(1)
    assert list_.containsNodeWithValue(2)
    assert list_.containsNodeWithValue(3)
    assert not list_.containsNodeWithValue(4)

    new_node = Node("new")
    list_.insertBefore(one, new_node)
    assert list_.getHead() is new_node
    list_.remove(new_node)
    assert list_.getHead() is one

    list_.insertAfter(three, new_node)
    assert list_.getTail() is new_node
    list_.remove(new_node)
    assert list_.getTail() is three

    list_.insertAtPosition(1, new_node)
    assert list_.getHead() is new_node
    list_.remove(new_node)
    list_.getHead() is one
    list_.getTail() is three

    list_.insertAtPosition(4, new_node)
    assert list_.getTail() is new_node
    list_.remove(new_node)
    list_.getTail() is three
    list_.getHead() is one

    list_.removeNodesWithValue(1)
    assert list_.getHead() is two

    one = Node(1)
    two = Node(2)
    three = Node(3)


def test_two():
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)

    one.next = two
    two.prev = one
    two.next = three
    three.prev = two
    three.next = four
    four.prev = three
    four.next = five
    five.prev = four

    list_ = DoublyLinkedList()
    list_.setHead(one)
    list_.setTail(five)

    six = Node(6)
    another_three = Node(3)
    another_another_three = Node(3)

    list_.setHead(four)
    list_.setTail(six)
    list_.insertBefore(six, three)
    list_.insertAfter(six, another_three)
    list_.insertAtPosition(1, another_another_three)
    list_.removeNodesWithValue(3)
    list_.remove(two)
    assert list_.containsNodeWithValue(5)


if __name__ == "__main__":
    test_one()
    test_two()
