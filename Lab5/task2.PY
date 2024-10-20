import heapq
from typing import Dict, List, Tuple
import task1 as t1

def manhattanDistance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def createGraphFromMaze(maze: List[str]) -> Tuple[t1.Graph, Tuple[int, int], Tuple[int, int]]:
    graph = t1.Graph()
    rows, cols = len(maze), len(maze[0])
    start, end = None, None
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] in '0SE':
                node = f"{i},{j}"
                if maze[i][j] == 'S':
                    start = (i, j)
                elif maze[i][j] == 'E':
                    end = (i, j)
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and maze[ni][nj] in '0SE':
                        neighbor = f"{ni},{nj}"
                        graph.addEdge(node, neighbor, 1)
    
    return graph, start, end

def solveMaze(maze: List[str]) -> Tuple[List[Tuple[int, int]], int]:
    graph, start, end = createGraphFromMaze(maze)
    rows, cols = len(maze), len(maze[0])
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] in '0SE':
                node = f"{i},{j}"
                graph.addHeuristic(node, manhattanDistance((i, j), end))
    
    start_node = f"{start[0]},{start[1]}"
    end_node = f"{end[0]},{end[1]}"
    
    path, cost = t1.aStarSearch(graph, start_node, end_node)
    
    coord_path = [tuple(map(int, node.split(','))) for node in path]
    
    return coord_path, cost

# Example usage
maze = [
    "00010",
    "11010",
    "00010",
    "01100",
    "S000E"
]

optimal_path, total_cost = solveMaze(maze)
print(f"Optimal path: {optimal_path}")
print(f"Total cost: {total_cost}")
