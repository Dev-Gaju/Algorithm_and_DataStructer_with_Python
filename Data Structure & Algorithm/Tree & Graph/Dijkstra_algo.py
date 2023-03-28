import heapq

class Edge:
    def __init__(self, dest, weight):
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, src, dest, weight):
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dest not in self.adj_list:
            self.adj_list[dest] = []
        self.adj_list[src].append(Edge(dest, weight))
        self.adj_list[dest].append(Edge(src, weight))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.adj_list}
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            (current_dist, current_vertex) = heapq.heappop(heap)

            if current_dist > distances[current_vertex]:
                continue

            for edge in self.adj_list[current_vertex]:
                distance = current_dist + edge.weight

                if distance < distances[edge.dest]:
                    distances[edge.dest] = distance
                    heapq.heappush(heap, (distance, edge.dest))

        return distances
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 8)
g.add_edge('C', 'E', 10)
g.add_edge('D', 'E', 2)

distances = g.dijkstra('A')
print(distances)
# Output: {'A': 0, 'B': 3, 'C': 2, 'D': 8, 'E': 10}
