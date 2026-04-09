from queue import Queue


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        self.bfs(self, array)
        return array

    def bfs(self, node, array):
        q = Queue()
        q.put(node)

        while q.qsize() > 0:
            v = q.get()
            array.append(v.name)

            for child in v.children:
                q.put(child)

            q.task_done()


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
    root.breadthFirstSearch(array)
    print(array)


if __name__ == "__main__":
    test()
