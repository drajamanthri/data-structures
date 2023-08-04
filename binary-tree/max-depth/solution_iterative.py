class Node:
    def __init__(self, val):
        self.left:Node = None 
        self.right:Node = None 
        self.value:Node = val 
        self.depth:int = 0

class Tree:
    def __init__(self, root:Node):
        self.root:Node = root

    '''
    This function returns the max depth of the tree with root 
    provided for the constructor using iterative depth first traversal.
    DFS type: post order
    '''
    def max_depth(self):

        if self.root is None:
            #if there are no nodes, the depth is -1
            return -1
        
        max_depth = -1
        self.root.depth = 0
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.depth > max_depth:
                max_depth = node.depth

            if node.left is not None:
                node.left.depth = node.depth + 1
                stack.append(node.left)

            if node.right is not None:
                node.right.depth = node.depth + 1
                stack.append(node.right)

        return max_depth
        
'''     
        1
    2       3
4       5
    6
max depth = 2
Test by changing the tree
'''
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3 
n2.left = n4 
n2.right = n5 
n5.left = n6

t = Tree(n1)
print(t.max_depth())