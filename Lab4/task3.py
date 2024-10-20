
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_tree1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(8)
    return root


def create_tree2():
    root = TreeNode(50)
    root.left = TreeNode(17)
    root.right = TreeNode(76)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(23)
    root.left.left.left = TreeNode(14)
    root.left.left.left.left = TreeNode(12)
    root.left.right.left = TreeNode(19)
    root.right.left = TreeNode(54)
    root.right.left.right = TreeNode(72)
    root.right.left.right.left = TreeNode(67)
    return root


def pre_order(node):
    if node:
        print(node.value, end=' ')
        pre_order(node.left)
        pre_order(node.right)


def in_order(node):
    if node:
        in_order(node.left)
        print(node.value, end=' ')
        in_order(node.right)


def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.value, end=' ')

if __name__ == '__main__':
    tree1 = create_tree1()
    tree2 = create_tree2()

    print("Tree 1 Traversals:")
    print("Pre-Order:", end=' ')
    pre_order(tree1)
    print("\nIn-Order:", end=' ')
    in_order(tree1)
    print("\nPost-Order:", end=' ')
    post_order(tree1)

    print("\n\nTree 2 Traversals:")
    print("Pre-Order:", end=' ')
    pre_order(tree2)
    print("\nIn-Order:", end=' ')
    in_order(tree2)
    print("\nPost-Order:", end=' ')
    post_order(tree2)