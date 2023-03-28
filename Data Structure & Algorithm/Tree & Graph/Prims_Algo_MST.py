import heapq

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class Graph:
    def __init__(self, edges, vertices):
        self.edges = edges
        self.vertices = vertices
        self.adj_list = {vertex: [] for vertex in vertices}

        for edge in edges:
            self.adj_list[edge.src].append(edge)
            self.adj_list[edge.dest].append(Edge(edge.dest, edge.src, edge.weight))

    def prims_algorithm(self):
        start_vertex = self.vertices[0]
        visited = {vertex: False for vertex in self.vertices}
        visited[start_vertex] = True
        heap = self.adj_list[start_vertex]
        heapq.heapify(heap)
        mst = []
        while heap:
            edge = heapq.heappop(heap)
            if visited[edge.dest]:
                continue
            visited[edge.dest] = True
            mst.append(edge)
            for neighbor_edge in self.adj_list[edge.dest]:
                if not visited[neighbor_edge.dest]:
                    heapq.heappush(heap, neighbor_edge)
        return mst
edges = [
    Edge('A', 'B', 4),
    Edge('A', 'C', 1),
    Edge('A', 'D', 3),
    Edge('B', 'C', 2),
    Edge('B', 'E', 3),
    Edge('C', 'D', 2),
    Edge('C', 'E', 5),
    Edge('C', 'F', 4),
    Edge('D', 'F', 6),
    Edge('E', 'F', 4),
]

vertices = ['A', 'B', 'C', 'D', 'E', 'F']

g = Graph(edges, vertices)
mst = g.prims_algorithm()

for edge in mst:
    print(f"{edge.src} -- {edge.dest}: {edge.weight}")
