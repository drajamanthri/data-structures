class Node:
    def __init__(self, value:int):
        self.left:Node = None
        self.right:Node = None
        self.value:int = value

class Tree:
    '''
    This function traverse the left and right nodes of the given node
    iteratively and count nodes that are greater or equal to the to 
    the nodes in the path from root.

    @param self
    @param node:Node traversing node
    '''
    def dfs(self, node:Node):
        if node is None:
            return 0
        
        count = 0 #keeps track of matching nodes

        stack = [(node, float('-inf'))] # (node, currentMax)

        while stack:
            #get the top item from the stack
            node, currentMax = stack.pop()
            if node.value >= currentMax:
                #if the node value is greater or equal to the current max
                # increment the count and update the current max
                count += 1
                currentMax = node.value
            
            if node.left:
                #if the left child is set, add it to stack
                stack.append((node.left, currentMax))

            if node.right:
                #if the right child is set, add it to the stack
                stack.append((node.right, currentMax))

        return count


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
print(tree.dfs(n1))
