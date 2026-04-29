class MinHeap:
    def __init__(self, array):
        self.heap = []
        self.buildHeap(array)

    def buildHeap(self, array):
        for el in array:
            self.insert(el)

    def siftDown(self, index):
        if index >= len(self.heap):
            return

        smallest_i = index
        left_i = self._get_left_child_index(index)
        right_i = self._get_right_child_index(index)

        if left_i < len(self.heap) and self.heap[left_i] < self.heap[smallest_i]:
            smallest_i = left_i
        if right_i < len(self.heap) and self.heap[right_i] < self.heap[smallest_i]:
            smallest_i = right_i

        if smallest_i != index:
            self.heap[index], self.heap[smallest_i] = (
                self.heap[smallest_i],
                self.heap[index],
            )
            self.siftDown(smallest_i)

    def siftUp(self, index):
        if index <= 0:
            return

        parent_index = self._get_parent_index(index)
        parent_value = self.heap[parent_index]
        current_value = self.heap[index]

        if current_value < parent_value:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
            self.siftUp(parent_index)

    def peek(self):
        if not self.heap:
            return
        return self.heap[0]

    def remove(self):
        if not self.heap:
            return

        self.heap[0], self.heap[len(self.heap) - 1] = (
            self.heap[len(self.heap) - 1],
            self.heap[0],
        )
        out = self.heap.pop()
        self.siftDown(0)
        return out

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def _get_parent_index(self, index):
        return (index - 1) // 2

    def _get_left_child_index(self, index):
        return 2 * index + 1

    def _get_right_child_index(self, index):
        return 2 * index + 2
