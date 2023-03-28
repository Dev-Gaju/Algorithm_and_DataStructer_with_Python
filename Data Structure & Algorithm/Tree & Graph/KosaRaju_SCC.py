from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited, stack):
        visited.add(v)
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited, stack)
        stack.append(v)

    def transpose(self):
        g = Graph(self.V)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                g.addEdge(neighbor, vertex)
        return g

    # def SCC(self):
    #     visited = set()
    #     stack = []
    #     for vertex in self.graph:
    #         if vertex not in visited:
    #             self.DFSUtil(vertex, visited, stack)
    #     transposed_graph = self.transpose()
    #     visited.clear()
    #     sccs = []
    #     while stack:
    #         v = stack.pop()
    #         if v not in visited:
    #             scc = set()
    #             transposed_graph.DFSUtil(v, visited, scc)
    #             sccs.append(scc)
    #     return sccs
    def SCC(self):
        visited = set()
        stack = []
        for vertex in list(self.graph.keys()):
            if vertex not in visited:
                self.DFSUtil(vertex, visited, stack)
        transposed_graph = self.transpose()
        visited.clear()
        sccs = []
        for v in reversed(stack):
            if v not in visited:
                scc = []
                transposed_graph.DFSUtil(v, visited, scc)
                sccs.append(scc)
        return sccs


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

sccs = g.SCC()
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)

