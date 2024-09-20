
class UndirectedGraph:
    graph = {}
    
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        self.graph[vertex] = []
        
    def add_edge(self,vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        
    def get_degree(self, vertex):
        return len(self.graph[vertex])
        

if __name__ == "__main__":
    graph = UndirectedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_edge(1, 2)
    print(graph.graph)