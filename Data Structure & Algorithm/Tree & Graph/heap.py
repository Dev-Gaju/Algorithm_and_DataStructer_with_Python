class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1
        while i != 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def delete_min(self):
        if len(self.heap) == 0:
            return None
        min_item = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.min_heapify(0)
        return min_item

    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.swap(i, smallest)
            self.min_heapify(smallest)

    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) // 2, -1, -1):
            self.min_heapify(i)
# create an empty min-heap
heap = MinHeap()

# insert some items
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(4)

# delete the minimum item
min_item = heap.delete_min()
print(min_item)  # should print 1

# build a heap from an array
arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
heap.build_heap(arr)
min_item = heap.delete_min()
print(min_item)  # should print 1 again


# heap = MinHeap()
# heap.heap = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# heap.min_heapify(0)
