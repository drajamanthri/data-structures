from collections import deque

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    '''
    This function prints each node value of the binary tree given by the root by using bfs
    '''
    def bfs(self, root):
        if root is None:
            return

        q = deque([root])
        while q:
            node = q.popleft()
            print(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.left = n2
n1.right = n3

t = Tree()
t.bfs(n1)

        

    
