
class UndirectedGraph:
    graph = {}
    
    def __init__(self):
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            
    def add_edge(self,vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)
        
    def get_degree(self, vertex):
        return len(self.graph[vertex])
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex} : {self.graph[vertex]}")
        
    
    def find_path(self, start, end):
        queue = [[start]]  
        visited = set() 
        
        if start == end:
            return [start]
        
        while queue:
            path = queue.pop(0)  
            node = path[-1]  
            
            if node not in visited:
                neighbors = self.graph[node]  
                
                for neighbor in neighbors:
                    new_path = path + [neighbor]  
                    
                    if neighbor == end:
                        return new_path  
                    
                    queue.append(new_path)  
                
                visited.add(node)  
        
        return None  
    

    def find_all_paths(self, start, end):
        stack = [[start]]  
        all_paths = []  
        visited = set()  
        
        while stack:
            path = stack.pop()  
            node = path[-1]  
            
            if node == end:
                all_paths.append(path)  
            else:
                if node not in visited:
                    neighbors = self.graph[node]  
                    
                    for neighbor in neighbors:
                        if neighbor not in path:  
                            new_path = path + [neighbor]  
                            stack.append(new_path) 
                    
                    visited.add(node) 
        
        return all_paths  
    
    
    def create_graph_from_table(self,table):
        graph = UndirectedGraph()
        rows = len(table)
        cols = len(table[0])

        for row in table:
            for value in row:
                graph.add_vertex(value)

        for i in range(rows):
            for j in range(cols):
                current_value = table[i][j]
                
                if j + 1 < cols:
                    graph.add_edge(current_value, table[i][j + 1])
                    
                if i + 1 < rows:
                    graph.add_edge(current_value, table[i + 1][j])

        self.graph = graph.graph



if __name__ == "__main__":
    graph = UndirectedGraph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_edge(1, 2)
    vertices = [1,2,3,4,5,6]
    for vertex in vertices:
        graph.add_vertex(vertex)

    edges = [
        (6,4),(4,3),(4,5),(5,2),(3,2),(5,1),(1,2)
    ]

    for edge in edges:
        graph.add_edge(edge[0], edge[1])
        
    print(graph.graph)

    start_node = 6
    end_node = 1
    path = graph.find_path(start_node, end_node)
    
    if path:
        print(f"Path from {start_node} to {end_node}: {path}")
    else:
        print(f"No path found between {start_node} and {end_node}")
        
    all_paths = graph.find_all_paths(start_node, end_node)
    print(all_paths)
    table = [
        [100, 110, 120, 130],
        [140, 145, 45, 135],
        [220, 10, 165, 80],
        [180, 200, 191, 118]
    ]
    
    # Generate the graph
    graph.create_graph_from_table(table)
    
    # Print the graph
    graph.print_graph()