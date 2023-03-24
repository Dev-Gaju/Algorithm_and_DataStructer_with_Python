from collections import defaultdict


class Graph:

    def __init__(self, n):

        self.graph = defaultdict(list)

        self.N = n

    def addEdge(self, m, n):

        self.graph[m].append(n)

    def sortUtil(self, n, visited, stack):

        visited[n] = True

        for element in self.graph[n]:

            if not visited[element]:
                self.sortUtil(element, visited, stack)

        stack.insert(0, n)

    def topologicalSort(self):

        visited = [False] * self.N

        stack = []

        for element in range(self.N):

            if not visited[element]:
                self.sortUtil(element, visited, stack)

        print(stack)


graph = Graph(5)
graph.addEdge(0, 1)
graph.addEdge(0, 3)
graph.addEdge(1, 2)
graph.addEdge(2, 3)
graph.addEdge(2, 4)
graph.addEdge(3, 4)

print("The Topological Sort Of The Graph Is:  ")

graph.topologicalSort()
