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
    
    def find_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []

        path = path + [start_vertex]
        
        if start_vertex == end_vertex:
            return path
        
        if start_vertex not in self.graph:
            return None

        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:  
                new_path = self.find_path(neighbor, end_vertex, path)
                if new_path:
                    return new_path
        return None 
    
    
    
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

    vertex = 'E'
    out_degree, in_degree = g.get_degree(vertex)
    print(f"Vertex {vertex} - Out Degree: {out_degree}, In Degree: {in_degree}")
    
    start_vertex = 'A'
    end_vertex = 'F'
    path = g.find_path(start_vertex, end_vertex)

    if path:
        print(f"Path between {start_vertex} and {end_vertex}: {path}")
    else:
        print(f"No path found between {start_vertex} and {end_vertex}")