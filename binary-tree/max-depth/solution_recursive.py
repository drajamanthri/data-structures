class Node:
    def __init__(self, val):
        self.left:Node = None 
        self.right:Node = None 
        self.value:Node = val 

class Tree:
    def __init__(self, root:Node):
        self.root:Node = root

    '''
    This function returns the max depth of the tree with root 
    provided for the constructor using recursive depth first traversal.
    DFS type: post order
    '''
    def max_depth(self):
        if self.root is None:
            #if there are no nodes, the depth is -1
            return -1
        
        return self.max_depth_dfs(self.root)
        
    def max_depth_dfs(self, node:Node):
        if node is None:
            return -1
        
        #depth of a node = max of left depth and right depth + 1
        #+1 because its the depth of the current node

        left_depth = self.max_depth_dfs(node.left)
        right_depth = self.max_depth_dfs(node.right)
        depth = max(left_depth, right_depth)

        return depth + 1


'''     
        1
    2       3
4
max depth = 2
Test by changing the tree
'''
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.left = n2
n1.right = n3 
n2.left = n4 

t = Tree(n1)
print(t.max_depth())