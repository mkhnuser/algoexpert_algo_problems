FLOAT_INCREMENT = 0.5


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    original_head = head
    loop_node = None

    while head is not None:
        if not float(head.value).is_integer():
            loop_node = head
            break

        head.value += FLOAT_INCREMENT
        head = head.next

    head = original_head

    counter = 0
    while head is not None:
        if head is loop_node:
            counter += 1
            if counter == 2:
                # NOTE: At this point we've encoutered the loop node for the second time.
                # Therefore, all the values have been restored.
                break

        head.value -= FLOAT_INCREMENT
        head.value = int(head.value)
        head = head.next

    return loop_node


def print_list(node):
    while node is not None:
        print(node.value)
        node = node.next


def test():
    one = LinkedList(value=1)
    two = LinkedList(value=2)
    three = LinkedList(value=3)

    one.next = two
    two.next = three
    three.next = two

    assert findLoop(one) is two


if __name__ == "__main__":
    test()
