class DirectedGraph:
    graph = {}
    
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        self.graph[vertex] = []
        
    def add_edge(self,vertex1, vertex2, isForwards = True):
        if isForwards:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex2].append(vertex1)
        
    def get_degree(self, vertex):
        inDegree = 0
        for x in self.graph:
            if vertex in self.graph[x]:
                inDegree += 1
        return (len(self.graph[vertex]), inDegree)
    
   
    def find_path(self, start_vertex, end_vertex):
        path = []
        stack = [(start_vertex, [start_vertex])]
        
        while stack:
            (vertex, current_path) = stack.pop()
            
            if vertex == end_vertex:
                return current_path
            
            for neighbor in self.graph[vertex]:
                if neighbor not in current_path:
                    stack.append((neighbor, current_path + [neighbor]))
                    
        return None

    
    def find_all_paths(self, start_vertex, end_vertex):
        all_paths = []
        stack = [(start_vertex, [start_vertex])]
        
        while stack:
            (vertex, current_path) = stack.pop()
            
            if vertex == end_vertex:
                all_paths.append(current_path)
            else:
                for neighbor in self.graph[vertex]:
                    if neighbor not in current_path:
                        stack.append((neighbor, current_path + [neighbor]))
        
        return all_paths
    
    
    
if __name__ == "__main__":
    g = DirectedGraph()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for vertex in vertices:
        g.add_vertex(vertex)

    edges = [
        ('A', 'B'),
        ('B', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'E'),
        ('D', 'E'),
        ('E', 'F'),
        ('G', 'D')
    ]

    for edge in edges:
        g.add_edge(edge[0], edge[1])

    print("Graph structure:", g.graph)

    for x in g.graph:
        out_degree, in_degree = g.get_degree(x)
        print(f"{x}:OutDegree: {out_degree}, InDegree: {in_degree}")
    
    start_vertex = 'A'
    end_vertex = 'F'
    path = g.find_path(start_vertex, end_vertex)
    print(f"path: {path}")
        
    all_paths = g.find_all_paths(start_vertex, end_vertex)

    print(f"all paths: {all_paths}")