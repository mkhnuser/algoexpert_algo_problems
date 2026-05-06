class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        # NOTE: The most craziest thing I've ever seen is to return self.
        # Man, you are sick. As sick as one can be.
        return self

    def depthFirstSearch(self, array):
        return self.iterative_solution(array)

    def iterative_solution(self, array):
        stack = [self]

        while stack:
            c = stack.pop()
            array.append(c.name)
            for child in reversed(c.children):
                stack.append(child)

        return array

    def recursive_solution(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array


def test():
    root = Node("A")
    b = Node("B")
    e = Node("E")
    f = Node("F")
    i = Node("I")
    j = Node("J")
    c = Node("C")
    d = Node("D")
    g = Node("G")
    k = Node("K")
    h = Node("H")

    root.children.extend([b, c, d])
    b.children.extend([e, f])
    f.children.extend([i, j])
    d.children.extend([g, h])
    g.children.extend([k])

    array = []
    root.depthFirstSearch(array)
    print(array)


if __name__ == "__main__":
    test()
