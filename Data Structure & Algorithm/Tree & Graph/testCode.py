class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return i // 2

    def left_child(self, i):
        return 2 * i

    def right_child(self, i):
        return 2 * i + 1

    def swap(self, i,j):
        self.heap[i], self.heap[j]  =self.heap[j], self.heap[i]

    def insert_val(self, val):
        self.heap.append(val)
        i = len(self.heap)-1
        while i !=0 and self.heap[i] < self.heap[self.parent(i)]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def delete(self):
        if self.heap ==0:
            return 0
        min_heap = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.heapify(0)
        return  min_heap

    def heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest =left
        if right <len(self.heap)  and self.heap[right] <self.heap[smallest]:
            smallest = right
        if smallest !=i:
            self.swap(i, smallest)
            self.heapify(smallest)

heap = MinHeap()

# insert some items
heap.insert_val(3)
heap.insert_val(2)
heap.insert_val(5)
heap.insert_val(4)

print(heap.delete())