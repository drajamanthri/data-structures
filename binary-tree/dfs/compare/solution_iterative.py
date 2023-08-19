class Node:
    def __init__(self, val):
        self.val = val
        self.left:Node = None 
        self.right:Node = None 

class Tree:
    '''
    This function compare two binary trees given the root nodes iteratively
    @param self
    @param node1:Node the root node of tree1
    @param node2:Node the root node of tree2
    '''
    def compare(self, n1:Node, n2:Node):
        
        stack1 = [n1]
        stack2 = [n2]

        #we have to iterate each node of tree1 and compare with the 
        #corresponding node of tree2. If they match, continue for
        #all the nodes. If any of the node don't match, we can conclude 
        #that the trees don't match.
        while stack1 and stack2:
            a = stack1.pop()
            b = stack2.pop()
            if a is None and b is None:
                continue 
            elif a is None or b is None:
                return False
            elif a.val == b.val:
                stack1.append(a.left)
                stack1.append(a.right)
                stack2.append(b.left)
                stack2.append(b.right) 
            else:
                return False
            
        if not stack1 and not stack2:
            return True
        else: 
            return False

#test with different trees
n1 = Node(1)
n2 = Node(2)
n1.left = n2

n11 = Node(1)
n12 = Node(2)
n11.left = n12

t = Tree()
r = t.compare(None, None)
print(r)
        

