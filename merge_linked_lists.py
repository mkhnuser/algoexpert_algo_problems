class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def replicate_list(head):
    new_head = LinkedList(head.value)
    head = head.next
    current = new_head

    while head is not None:
        current.next = LinkedList(None)
        current = current.next
        current.value = head.value
        head = head.next

    return new_head


def merge_linked_lists(headOne, headTwo) -> LinkedList:
    if headOne.value < headTwo.value:
        new_head = LinkedList(headOne.value)
        headOne = headOne.next
    else:
        new_head = LinkedList(headTwo.value)
        headTwo = headTwo.next

    current = new_head
    o = headOne
    t = headTwo

    while o is not None and t is not None:
        current.next = LinkedList(None)
        current = current.next
        if o.value < t.value:
            current.value = o.value
            o = o.next
        else:
            current.value = t.value
            t = t.next

    if o is not None:
        current.next = replicate_list(o)

    if t is not None:
        current.next = replicate_list(t)

    return new_head


def mergeLinkedLists(headOne, headTwo):
    if headOne is None and headTwo is None:
        return None
    if headOne is None:
        return replicate_list(headOne)
    if headTwo is None:
        return replicate_list(headTwo)
    return merge_linked_lists(headOne, headTwo)
