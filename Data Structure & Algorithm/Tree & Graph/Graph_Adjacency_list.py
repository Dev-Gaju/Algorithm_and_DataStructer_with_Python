class Edges:
    def __init__(self, src, dest):
        self.source = src
        self.destination = dest


"""
In graph assign in memory with Adjacency matrix
This is an Unweighted Graph
1. Create Graph & Print
2. Find Any Vertex's Neighbour 
3. Find Shortest Path
4. BFS & DFS
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

    def findAnyNeighbours(self, src):
        for source, destination in self.adjacency_List.items():
            if source == src:
                for dest in destination:
                    print(dest, end=" ")

    def bfsOrder(self, start_node):  # O(V=E)
        visited = set()  # keep track on visited
        queue = []  # store node to visited
        visited.add(start_node)
        queue.append(start_node)
        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")

            # add adjacent node to queue
            if current_node in self.adjacency_List:
                for adjacent_node in self.adjacency_List[current_node]:
                    if adjacent_node not in visited:
                        visited.add(adjacent_node)
                        queue.append(adjacent_node)

    def dfsOrder(self, start_node, visited=None):
        if visited is None:
            visited = set()
        visited.add(start_node)
        print(start_node, end=" ")
        if start_node in self.adjacency_List:
            for adjacency_node in self.adjacency_List[start_node]:
                if adjacency_node not in visited:
                    self.dfsOrder(adjacency_node, visited)  # recursion used


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
# graph.findAnyNeighbours(1)
# graph.bfsOrder(0)
graph.dfsOrder(0)
