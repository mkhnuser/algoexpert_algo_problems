import heapq


class ContinuousMedianHandler:
    def __init__(self):
        self.small = []  # NOTE: Let it be max heap.
        self.large = []  # NOTE: Let it be min heap.

    def insert(self, number):
        heapq.heappush(self.small, -number)
        # NOTE: Ensure every value in the small heaps <= every value in the large heap.
        if self.small and self.large and (-self.small[0] > self.large[0]):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def getMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((-self.small[0]) + self.large[0]) / 2
