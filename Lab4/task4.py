
image = [
    [150, 2, 5],
    [80, 145, 45],
    [74, 102, 165]
]


def create_graph(image):
    graph = {}
    rows, cols = len(image), len(image[0])
    
    for i in range(rows):
        for j in range(cols):
            pixel = image[i][j]
            neighbors = []
            
            # Check 4-connectivity: up, down, left, right
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    neighbors.append(image[ni][nj])
            
            graph[pixel] = neighbors
    
    return graph


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


graph = create_graph(image)

print("DFS traversal starting from pixel 150:")
dfs(graph, 150)