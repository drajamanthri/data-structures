class Node:
    def __init__(self, value:int):
        self.left:Node = None
        self.right:Node = None
        self.value:int = value

class Tree:
    '''
    This function traverse the left and right nodes of the given node
    recursively and count nodes that are greater or equal to the to 
    the nodes in the path from root.

    @param self
    @param node:Node traversing node
    '''
    def dfs(self, node:Node, currentMax:int):
        if node is None:
            return 0
        
        #process node
        count = 0
        if node.value >= currentMax:
            #if node value is greater or equal to the current max,
            # increment count and update current max.
            count += 1
            currentMax = node.value

        left = self.dfs(node.left, currentMax)
        right = self.dfs(node.right, currentMax)

        return count + left + right


#Test with different node configurations
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
'''
        1
    2       3
4
'''
n1.left = n3 
n1.right = n5 
n3.left = n2
n2.left = n4 

tree = Tree()
print(tree.dfs(n1, float("-inf")))
