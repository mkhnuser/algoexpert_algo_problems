class MinMaxStack:
    def __init__(self) -> None:
        self.items = []
        self.max_items = []
        self.min_items = []

    def peek(self):
        if not self.items:
            raise Exception("No items!")

        return self.items[-1]

    def pop(self):
        if not self.items:
            raise Exception("No items!")

        popped = self.items.pop()

        if popped == self.min_items[-1]:
            self.min_items.pop()
        if popped == self.max_items[-1]:
            self.max_items.pop()

        return popped

    def push(self, number):
        if not self.min_items or number <= self.min_items[-1]:
            self.min_items.append(number)

        if not self.max_items or number >= self.max_items[-1]:
            self.max_items.append(number)

        self.items.append(number)

    def getMin(self):
        return self.min_items[-1]

    def getMax(self):
        return self.max_items[-1]


def test():
    stack = MinMaxStack()
    stack.push(5)

    assert stack.getMin() == 5
    assert stack.getMax() == 5
    assert stack.peek() == 5

    stack.push(7)
    assert stack.getMin() == 5
    assert stack.getMax() == 7
    assert stack.peek() == 7

    stack.push(2)
    assert stack.getMin() == 2
    assert stack.getMax() == 7
    assert stack.peek() == 2

    assert stack.pop() == 2
    assert stack.pop() == 7
    assert stack.getMin() == 5
    assert stack.getMax() == 5
    assert stack.peek() == 5


if __name__ == "__main__":
    test()
