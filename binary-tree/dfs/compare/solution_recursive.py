class Node:
    def __init__(self, val):
        self.val:int = val
        self.left:Node = None 
        self.right:Node = None 

class Tree:
    '''
    This function compare two binary trees given the root nodes
    @param self
    @param node1:Node the root node of tree1
    @param node2:Node the root node of tree2
    '''
    def compare(self, node1:Node, node2:Node):
        if node1 is None and node2 is None:
            #if both nodes are none, we consider the trees are equal
            return True
        elif node1 is None or node2 is None:
            #if only one node is none, the trees are different
            return False
        elif node1.val == node2.val and self.compare(node1.left, node2.left) and self.compare(node1.right, node2.right):
            #if both nodes are not none, we consider the trees are equal if
            # node1 value == node2 value and left subtrees are equal and right subtrees are equal
            return True
        else:
            #in all the other cases, the trees are not equal
            return False

#test with different trees
n1 = Node(1)
n2 = Node(2)
n1.left = n2

n11 = Node(1)
n12 = Node(2)
n11.right = n12

t = Tree()
r = t.compare(n1, n11)
print(r)


