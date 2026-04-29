class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def moveTail(head):
    original_head = head

    while head.next.next is not None:
        head = head.next

    pre_tail = head
    tail = head.next
    pre_tail.next = None
    tail.next = original_head
    return tail


def moveHead(head):
    original_head = head
    new_head = original_head.next

    while head.next is not None:
        head = head.next

    tail = head
    tail.next = original_head
    original_head.next = None
    return new_head


def shiftLinkedList(head, k):
    if head is None:
        return None

    if k == 0 or head.next is None:
        return head

    # NOTE: At this point,
    # k >= 1 and the length of the list is at least two.

    if k > 0:
        # NOTE:
        # 1. Locate the tail.
        # 2. Delete the tail.
        # 3. Prepend the tail to the start of the list.
        # 4. Continue steps 1. - 3. k times.
        for _ in range(k):
            head = moveTail(head)
    else:
        # NOTE: k < 0 at this point.
        # NOTE:
        # 1. Locate the head.
        # 2. Delete the head.
        # 3. Append the head to the end of the list.
        # 4. Continue steps 1. - 3. abs(k) times.
        for _ in range(abs(k)):
            head = moveHead(head)

    return head
