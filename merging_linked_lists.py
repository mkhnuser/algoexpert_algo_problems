class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    if linkedListOne is None and linkedListTwo is None:
        return None
    if linkedListOne is None:
        return None
    if linkedListTwo is None:
        return None

    original_two = linkedListTwo

    while linkedListOne is not None:
        while linkedListTwo is not None:
            if linkedListOne is linkedListTwo:
                return linkedListTwo

            linkedListTwo = linkedListTwo.next

        linkedListOne = linkedListOne.next
        linkedListTwo = original_two

    return None
