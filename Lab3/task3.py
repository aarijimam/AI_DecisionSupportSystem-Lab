from collections import deque

def shortest_path_bfs(maze):
    if not maze or not maze[0]:
        return -1
    
    rows, cols = len(maze), len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    
    while queue:
        row, col, distance = queue.popleft()
        
        if row == rows - 1 and col == cols - 1:
            return distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            

            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, distance + 1))
    return -1

if __name__ == "__main__":
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # Find the shortest path
    result = shortest_path_bfs(maze)
    print("Shortest path length:", result)