class Edges:
    def __init__(self, src, dest, wt):
        self.source = src
        self.destination = dest
        self.weight = wt


"""
1. Create weighted Graph & Print (V^2) space  
2. Find Any Vertex's Neighbour
3. Find Shortest Path
"""

class Graph:
    def __init__(self):
        self.adjacency_List = {}

    def addEdges(self, a, b,c):
        edges = Edges(a, b,c)
        if edges.source not in self.adjacency_List:
            self.adjacency_List[edges.source] = []
        self.adjacency_List[edges.source].append((edges.destination, edges.weight))

    def printGraph(self):
        for source, destinations in self.adjacency_List.items():
            for a, b in destinations:
                print(f"{source}---{a,b}")

    def findAnyNeighbours(self, src):
        for source, destination in self.adjacency_List.items():
            if source == src:
                for dest,weight in destination:
                    print(dest, weight)


graph = Graph()
graph.addEdges(0, 2,2)
graph.addEdges(1, 2,10)
graph.addEdges(1, 3,0)
graph.addEdges(2, 0,2)
graph.addEdges(2, 1,10)
graph.addEdges(2, 3,-1)
graph.addEdges(3, 1,0)
graph.addEdges(3, 2,-1)
# graph.printGraph()
graph.findAnyNeighbours(2)
