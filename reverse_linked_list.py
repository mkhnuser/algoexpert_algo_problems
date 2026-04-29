class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    if head is None:
        return None
    if head.next is None:
        return head

    new_head = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return new_head
