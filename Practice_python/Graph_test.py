class Graph_test():
    def __init__(self, edges):
        self.edges = edges
        self.graph_dic ={}
        for start, end in edges:
            if start  in self.graph_dic:
                self.graph_dic[start].append(end)
            else:
                self.graph_dic[start]= [end]
        print("Start with all dictionaries: ", self.graph_dic)


    def get_all_path(self, start, end, path = []):
        path = path + [start]
        if start == end :
            return [path]
        if start not  in self.graph_dic:
            return None
        paths = []
        for node in self.graph_dic[start]:
            if node not  in path:
                new_path = self.get_all_path(node, end, path)
                for p in new_path:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path= []):
        path = path + [start]
        if start == end :
            return path
        if start not  in self.graph_dic:
            return  None
        shortest_path = None
        for node in self.graph_dic[start]:
            if node not in path:
                new_path = self.get_shortest_path(node,end,path)
                if shortest_path is  None or len(new_path) < len(shortest_path):
                    shortest_path = new_path
        return shortest_path





routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]
d = Graph_test(routes)
start = "Mumbai"
end = "New York"
print(f"path between Mumbai and New York:  ", d.get_all_path(start, end))
print(f"Shortest path between Mumbai and New York:  ", d.get_shortest_path(start, end))