class Edges:
    def __init__(self, src, dest):
        self.source = src
        self.destination = dest


"""
In graph assign in memory with Adjacency matrix

1------>0<------3
            |     ^
            v  /
            2  
            
"""


class Graph:
    def __init__(self):
        self.adjacency_List = {}

    def addEdges(self, a, b):
        edges = Edges(a, b)
        if edges.source not in self.adjacency_List:
            self.adjacency_List[edges.source] = []
        self.adjacency_List[edges.source].append(edges.destination)

    def isCycle(self):
        visited=set()
        rec_stack=set()
        def dfs(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbour in self.adjacency_List.get(node, []):
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
                elif neighbour in rec_stack:
                    return  True
            rec_stack.remove(node)
            return False
        for node in self.adjacency_List:
            if node not  in visited:
                if dfs(node):
                    return True
        return False

    def printGraph(self):
        for source, destinations in self.adjacency_List.items():
            for dest in destinations:
                print(f"{source}---{dest}")


graph = Graph()
graph.addEdges(1, 0)
graph.addEdges(0, 2)
graph.addEdges(2, 3)
graph.addEdges(3, 0)
# graph.printGraph()

if graph.isCycle():
    print("This graph is Cyclic")
else:
    print("No cycle")