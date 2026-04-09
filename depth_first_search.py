class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        self.dfs(self, array)
        return array

    def dfs(self, node, output):
        for child in node.children:
            output.append(child.name)
            self.dfs(child, output)


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
