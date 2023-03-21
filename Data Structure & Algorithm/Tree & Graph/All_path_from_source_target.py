class Edges:
    def __init__(self, src, dest):
        self.source = src
        self.destination = dest


"""
In graph assign in memory with Adjacency matrix
   1-----3 
  /         |  \
0          |   5---6
  \        |  /
   2-----4 
"""


class Graph:
    def __init__(self):
        self.adjacency_List = {}

    def addEdges(self, a, b):
        edges = Edges(a, b)
        if edges.source not in self.adjacency_List:
            self.adjacency_List[edges.source] = []
        self.adjacency_List[edges.source].append(edges.destination)

    def printGraph(self):
        for source, destinations in self.adjacency_List.items():
            for dest in destinations:
                print(f"{source}---{dest}")

    # modified DFS traversal
    def FindallPaths(self, source, target, path=[]):
        path = path + [source]
        if source == target:
            print(path)
        else:
            # recursively visit adjacent node
            if source in self.adjacency_List:
                for adjacent_node in self.adjacency_List[source]:
                    if adjacent_node not in path:
                        self.FindallPaths(adjacent_node, target, path)


graph = Graph()
graph.addEdges(0, 1)
graph.addEdges(0, 2)
graph.addEdges(1, 0)
graph.addEdges(1, 3)
graph.addEdges(2, 0)
graph.addEdges(2, 4)
graph.addEdges(3, 1)
graph.addEdges(3, 4)
graph.addEdges(3, 5)
graph.addEdges(4, 2)
graph.addEdges(4, 3)
graph.addEdges(4, 5)
graph.addEdges(5, 2)
graph.addEdges(4, 4)
graph.addEdges(4, 6)
graph.FindallPaths(0, 5)
