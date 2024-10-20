from task1 import *
if __name__ == '__main__':

    graph1 = {
        1: [2, 5],
        2: [1, 3, 5],
        3: [2, 4],
        4: [3, 5, 6],
        5: [1, 2, 4],
        6: [4]
    }

    
    graph2 = {
        'A': ['D', 'F'],
        'B': ['E', 'F'],
        'C': ['D'],
        'D': ['A', 'C'],
        'E': ['B'],
        'F': ['A', 'B']
    }
    
       
    print("Graph 1 DFS (starting from node 6):")
    print("Recursive:")
    dfs_recursive(graph1, 6)
    print("\nIterative:")
    dfs_iterative(graph1, 6)

    print("\n\nGraph 2 DFS (starting from node 'E'):")
    print("Recursive:")
    dfs_recursive(graph2, 'E')
    print("\nIterative:")
    dfs_iterative(graph2, 'E')