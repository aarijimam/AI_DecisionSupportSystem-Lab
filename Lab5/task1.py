import heapq
from typing import Dict, List, Tuple

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self) -> bool:
        return len(self.elements) == 0
    
    def putItem(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def getItem(self):
        return heapq.heappop(self.elements)[1]

class Graph:
    def __init__(self):
        self.edges: Dict[str, List[Tuple[str, int]]] = {}
        self.heuristics: Dict[str, int] = {}
    
    def addEdge(self, fromNode: str, toNode: str, cost: int):
        if fromNode not in self.edges:
            self.edges[fromNode] = []
        self.edges[fromNode].append((toNode, cost))
    
    def addHeuristic(self, node: str, value: int):
        self.heuristics[node] = value

def reconstructPath(cameFrom: Dict[str, str], start: str, goal: str) -> List[str]:
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = cameFrom[current]
    path.append(start)
    path.reverse()
    return path

def aStarSearch(graph: Graph, start: str, goal: str) -> Tuple[List[str], int]:
    frontier = PriorityQueue()
    frontier.putItem(start, 0)
    cameFrom: Dict[str, str] = {}
    costSoFar: Dict[str, int] = {}
    cameFrom[start] = None
    costSoFar[start] = 0
    
    while not frontier.isEmpty():
        current = frontier.getItem()
        
        if current == goal:
            break
        
        for nextNode, cost in graph.edges.get(current, []):
            newCost = costSoFar[current] + cost
            if nextNode not in costSoFar or newCost < costSoFar[nextNode]:
                costSoFar[nextNode] = newCost
                priority = newCost + graph.heuristics.get(nextNode, 0)
                frontier.putItem(nextNode, priority)
                cameFrom[nextNode] = current
    
    path = reconstructPath(cameFrom, start, goal)
    return path, costSoFar[goal]


graph = Graph()


edges = [
    ("Oradea", "Zerind", 71), ("Oradea", "Sibiu", 151),
    ("Zerind", "Arad", 75), ("Arad", "Sibiu", 140),
    ("Arad", "Timisoara", 118), ("Timisoara", "Lugoj", 111),
    ("Lugoj", "Mehadia", 70), ("Mehadia", "Dobreta", 75),
    ("Dobreta", "Craiova", 120), ("Craiova", "Rimnicu Vilcea", 146),
    ("Craiova", "Pitesti", 138), ("Sibiu", "Rimnicu Vilcea", 80),
    ("Sibiu", "Fagaras", 99), ("Rimnicu Vilcea", "Pitesti", 97),
    ("Fagaras", "Bucharest", 211), ("Pitesti", "Bucharest", 101),
    ("Bucharest", "Giurgiu", 90), ("Bucharest", "Urziceni", 85),
    ("Urziceni", "Vaslui", 142), ("Urziceni", "Hirsova", 98),
    ("Hirsova", "Eforie", 86), ("Vaslui", "Iasi", 92),
    ("Neamt", "Iasi", 87)
]

for edge in edges:
    graph.addEdge(edge[0], edge[1], edge[2])
    graph.addEdge(edge[1], edge[0], edge[2])  


heuristics = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Dobreta": 242,
    "Eforie": 161, "Fagaras": 178, "Giurgiu": 77, "Hirsova": 151,
    "Iasi": 226, "Lugoj": 244, "Mehadia": 241, "Neamt": 234,
    "Oradea": 380, "Pitesti": 98, "Rimnicu Vilcea": 193, "Sibiu": 253,
    "Timisoara": 329, "Urziceni": 80, "Vaslui": 199, "Zerind": 374
}

for node, value in heuristics.items():
    graph.addHeuristic(node, value)


start = "Arad"
goal = "Bucharest"
path, cost = aStarSearch(graph, start, goal)
print(f"Path from {start} to {goal}: {' -> '.join(path)}")
print(f"Total cost: {cost}")