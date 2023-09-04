from collections import defaultdict

class Graph:
    def __init__(self):
        #undirected_graph help us traverse all the nodes starting 
        #from node 0
        self.undirected_graph:defaultdict 
        # visited tracks all the traversed nodes and prevents infinite 
        # loops.
        self.visited:set
        #edges store the original edges and help us to decide if an edge
        #needs to be swapped.
        self.edges:set   

        self.count:int

    '''
    @param self
    @param edges:list[list] edges as a list
    @return # of edges which needs to be swapped to make all the edges
    Directed towards the zero node.
    '''
    def count(self, edges:list[list]):
        self.undirected_graph = defaultdict(list)
        self.visited = set()
        self.edges = set()
        self.count = 0

        for edge in edges:
            x,y = edge
            self.undirected_graph[x].append(y)
            self.undirected_graph[y].append(x)
            self.edges.add((x,y))

        self.dfs(0)

        return self.count

    def dfs(self, node:int):
        if node in self.visited:
            return
        
        self.visited.add(node)

        for neighbor in self.undirected_graph[node]:

            if neighbor not in self.visited:
                #Because self.edges is a set, it allows O(1) check
                if (node, neighbor) in self.edges:
                    self.count += 1

                self.dfs(neighbor)
        
    
graph = Graph()
#test with changing the inputs
edges = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(graph.count(edges))