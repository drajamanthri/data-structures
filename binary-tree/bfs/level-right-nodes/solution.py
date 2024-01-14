from collections import deque

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value 

class Tree:
    '''
    This function returns a list of right most node value of each level. 
    Assume root is not null;
    '''
    def find_level_right_nodes(self, root):
        q = deque([root])
        result = []

        while q:
            width = len(q)
            result.append(q[-1].val)

            for i in range(width):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
        return result
        
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.left = n2
n1.right = n3

t = Tree()
result = t.find_level_right_nodes(n1)
print(result)