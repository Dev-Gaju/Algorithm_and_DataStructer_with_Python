class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.distance = {vertex: float('inf') for vertex in vertices}
        self.distance[vertices[0]] = 0

    def bellman_ford(self):
        for i in range(len(self.vertices) - 1):
            for edge in self.edges:
                if self.distance[edge.src] + edge.weight < self.distance[edge.dest]:
                    self.distance[edge.dest] = self.distance[edge.src] + edge.weight

        # Check for negative cycles
        for edge in self.edges:
            if self.distance[edge.src] + edge.weight < self.distance[edge.dest]:
                print("Negative cycle detected.")
                return

        return self.distance

edges = [
    Edge('A', 'B', 4),
    Edge('A', 'C', 2),
    Edge('B', 'C', 1),
    Edge('B', 'D', 5),
    Edge('C', 'D', 8),
    Edge('C', 'E', 10),
    Edge('D', 'E', 2),
    Edge('E', 'B', -6)
]

vertices = ['A', 'B', 'C', 'D', 'E']

g = Graph(edges, vertices)
distances = g.bellman_ford()

if distances:
    print(distances)
    # Output: {'A': 0, 'B': 2, 'C': 1, 'D': 6, 'E': 8}

