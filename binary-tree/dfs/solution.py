class Node:
    def __init__(self, value:int):
        self.left:Node = None
        self.right:Node = None
        self.value:int = value

class Tree:
    '''
    This function traverse the left and right nodes of the given node
    recursively.

    This function uses pre order traversal.

    Pre order traversal: process node, traverse left, traverse right
    In order traversal: traverse left, process node, traverse right
    Post order traversal: traverse left, traverse right, process node
    @param self
    @param node:Node traversing node
    '''
    def dfs(self, node:Node):
        if node is None:
            return
        
        #process node
        print(node.value)
        self.dfs(node.left)
        self.dfs(node.right)


#Test with different node configurations
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

'''
        1
    2       3
4
'''
n1.left = n2 
n1.right = n3 
n2.left = n4 

tree = Tree()
tree.dfs(n1)
