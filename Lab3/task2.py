
class Tree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.middle = None
        self.right = None

def bfs(root):
    if root is None:
        return []

    queue = [root]
    bfs_order = []
    
    while queue:
        current_node = queue.pop(0)
        
        bfs_order.append(current_node.data)
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.middle:
            queue.append(current_node.middle)
        if current_node.right:
            queue.append(current_node.right)
    
    return bfs_order


root = Tree(1)
root.left = Tree(2)
root.middle = Tree(3)
root.right = Tree(4)
root.left.left = Tree(5)
root.left.right = Tree(6)
root.right.left = Tree(7)
root.right.right = Tree(8)
root.left.left.left = Tree(9)
root.left.left.right = Tree(10)
root.right.left.left = Tree(11)
root.right.left.right = Tree(12)


bfs_result = bfs(root)
print("BFS Traversal Order:", bfs_result)