import heapq
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
        
    def find_all_paths(self, start, end, path=None):
        if path is None:
            path = []
        
        path = path + [start]
        
        if start == end:
            return [path]

        if start not in self.graph:
            return []

        paths = []
        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end, path)
                for p in new_paths:
                    paths.append(p)
                    
        return paths

    def dijkstra(self, start_node):
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0
        visited = set()
        predecessors = {node: None for node in self.graph}

        while len(visited) < len(self.graph):
            current_node = None
            current_min_distance = float('inf')

            for node in distances:
                if node not in visited and distances[node] < current_min_distance:
                    current_min_distance = distances[node]
                    current_node = node

            if current_node is None:
                break

            visited.add(current_node)

            for neighbor in self.graph[current_node]:
                if neighbor not in visited:
                    weight = abs(current_node - neighbor)
                    new_distance = distances[current_node] + weight

                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        predecessors[neighbor] = current_node

        return distances, predecessors

    def shortest_path(self, start_node, end_node):
        distances, predecessors = self.dijkstra(start_node)

        path = []
        current_node = end_node
        while current_node is not None:
            path.insert(0, current_node)
            current_node = predecessors[current_node]

        if distances[end_node] == float('inf'):
            return None  
        else:
            return path, distances[end_node]
    
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
    for i in range(1,7):
        graph.add_vertex(i)
    edges = [
        (6,4),(4,3),(4,5),(5,2),(3,2),(5,1),(1,2)
    ]

    for edge in edges:
        graph.add_edge(edge[0], edge[1])
        
    print(graph.graph)
    for x in graph.graph:
        print(f"{x} : {graph.get_degree(x)}")

    start_node = 6
    end_node = 1
    path = graph.find_path(start_node, end_node)
    print(f"path: {path}")
    
        
    all_paths = graph.find_all_paths(start_node, end_node)
    print(f"all path: {all_paths}")
    
    table = [
        [100, 110, 120, 130],
        [140, 145, 45, 135],
        [220, 10, 165, 80],
        [180, 200, 191, 118]
    ]
    
    graph.create_graph_from_table(table)
    path = graph.find_path(100, 118)
    print(f"Path: {path}")
    
    all_paths = graph.find_all_paths(100, 118)
    print(f"Number of paths: {len(all_paths)}")
    shortest_path = graph.shortest_path(100, 118)
    print(f"Shortest path: {shortest_path}")