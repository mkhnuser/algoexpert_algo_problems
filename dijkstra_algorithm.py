import math


# NOTE: Every time, you try to find a global minimum out of some set.
# For this, a min heap is a perfect choice.


class MinHeap:
    def __init__(self):
        self.data = []  # NOTE: This array will be preserve min heap property.

    def insert(self, datum: int) -> None:
        """Insert an element into a min heap."""
        # NOTE: Append to the end.
        # Sift up.
        self.data.append(datum)
        self._sift_up(len(self.data) - 1)

    def delete(self) -> int:
        """Delete the min element from a min heap."""
        # NOTE: Pop the root.
        # Put the last element at the root.
        # Sift it down.
        # Return the popped root.
        if not self.data:
            raise Exception("The heap is empty.")

        out = self.data[0]
        new_root = self.data.pop()

        if not self.data:
            # NOTE: The out element was the only element present in the heap.
            return out

        self.data[0] = new_root
        self._sift_down(0)
        return out

    def _sift_up(self, index: int) -> None:
        if index == 0:
            return

        parent_index = self._get_parent_index(index)
        parent_element = self.data[parent_index]
        current_element = self.data[index]

        if parent_element > current_element:
            self.data[parent_index], self.data[index] = (
                self.data[index],
                self.data[parent_index],
            )
            self._sift_up(parent_index)

    def _sift_down(self, index: int) -> None:
        if index >= len(self.data):
            return

        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)
        min_element_index = index

        if (
            left_child_index < len(self.data)
            and self.data[left_child_index] < self.data[min_element_index]
        ):
            min_element_index = left_child_index
        if (
            right_child_index < len(self.data)
            and self.data[right_child_index] < self.data[min_element_index]
        ):
            min_element_index = right_child_index

        if min_element_index != index:
            self.data[min_element_index], self.data[index] = (
                self.data[index],
                self.data[min_element_index],
            )
            self._sift_down(min_element_index)

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _get_left_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def _get_right_child_index(self, index: int) -> int:
        return (2 * index) + 2


def find_min_distance_vertex(distances, visited):
    min_vertex = None
    min_distance = float("+inf")

    for v, dist in enumerate(distances):
        if distances[v] < min_distance and not visited[v]:
            min_distance = dist
            min_vertex = v

    return min_vertex


def dijkstrasAlgorithm(start, edges):
    # NOTE: A graph is directed.
    n = len(edges)
    distances = [float("+inf")] * n
    distances[start] = 0
    previous = [None] * n
    visited = [False] * n

    while True:
        c = find_min_distance_vertex(distances, visited)

        if c is None:
            break

        for neighbor, dist in edges[c]:
            dist_from_current = distances[c] + dist
            if distances[neighbor] > dist_from_current:
                distances[neighbor] = dist_from_current
                previous[neighbor] = c

        visited[c] = True

    return list(map(lambda x: x if not math.isinf(x) else -1, distances))


def test():
    edges = [
        [[1, 7]],  # 0
        [[2, 6], [3, 20], [4, 3]],  # 1
        [[3, 14]],  # 2
        [[4, 2]],  # 3
        [],  # 4
        [],  # 5
    ]
    print(dijkstrasAlgorithm(0, edges))


if __name__ == "__main__":
    test()
