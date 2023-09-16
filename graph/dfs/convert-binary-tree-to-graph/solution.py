from collections import defaultdict

class TreeNode:
    def __init__(self, val:int):
        self.value = val
        self.left:TreeNode = None
        self.right:TreeNode = None

class Tree:
    def __init__(self):
        self.root:TreeNode 

    '''
    This function convert the tree into a graph which is represented 
    by an adjacency list.
    The graph is undirected.
    '''
    def convert_to_graph(self)->defaultdict:
        graph = defaultdict(list)

        self.add_node_to_graph(self.root, graph)
        return graph

    def add_node_to_graph(self, node:TreeNode, graph:defaultdict):
        if node is None:
            return 
        
        value = node.value
        if node.left:
            left = node.left.value 
            #the graph is undirected. 
            #therefore, add edges for both direction.
            graph[value].append(left)
            graph[left].append(value)

        if node.right:
            right = node.right.value 
            graph[value].append(right)
            graph[right].append(value)

        #recursively add left and right subtrees into the graph
        self.add_node_to_graph(node.left, graph)
        self.add_node_to_graph(node.right, graph)
        

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n2
n1.right = n3 

tree = Tree()
tree.root = n1

print(tree.convert_to_graph())