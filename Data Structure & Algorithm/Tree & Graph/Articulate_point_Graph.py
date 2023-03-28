# graph = {'A': ['B', 'D'],
#          'B': ['A', 'C', 'E'],
#          'C': ['B', 'F'],
#          'D': ['A', 'E'],
#          'E': ['B', 'D', 'F'],
#          'F': ['C', 'E']}
def tarjan_ap(graph):
    ap = set()
    visited = set()
    low = {}
    disc = {}
    parent = {}

    def dfs(node, time):
        visited.add(node)
        disc[node] = time
        low[node] = time
        children = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                children += 1
                parent[neighbor] = node
                dfs(neighbor, time + 1)
                low[node] = min(low[node], low[neighbor])
                if parent[node] is None and children > 1:
                    ap.add(node)
                if parent[node] is not None and low[neighbor] >= disc[node]:
                    ap.add(node)
            elif neighbor != parent[node]:
                low[node] = min(low[node], disc[neighbor])

    for node in graph:
        if node not in visited:
            parent[node] = None
            dfs(node, 0)

    return ap
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}
ap = tarjan_ap(graph)
print(ap)
