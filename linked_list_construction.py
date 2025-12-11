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
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return

        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return

        node = self.head
        current_position = 1

        while node is not None and current_position != position:
            node = node.next
            current_position += 1

        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        head = self.head

        while head is not None:
            candidate = head
            head = head.next
            if candidate.value == value:
                self.remove(candidate)

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None

    def containsNodeWithValue(self, value):
        head = self.head

        while head is not None:
            if head.value == value:
                return True
            head = head.next

        return False
