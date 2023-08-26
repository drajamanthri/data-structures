from collections import defaultdict

class Graph:
    def __init__(self):
        self.neighbors:defaultdict
        self.visited:set

    '''
    This function returns the # of connected components of the graph given by the
    isConnected adjacency matrix
    @param self
    @param isConnected adjacency matrix 
    if graph[i][j] is 1, then the nodes i and j are connected
    Using an adjacency matrix is not an efficient way of getting the neighbors 
    of a node
    '''
    def count_connected_components(self, graph: list[list[int]]) -> int:

        self.neighbors = defaultdict(list)
        self.visited = set()
        n = len(graph[0])
        self.build_neighbors(graph)

        count = 0
        for i in range(n):
            #if a node is already visited, it is a part of an existing component (group)
            if i not in self.visited:
                count += 1
                self.dfs(i)

        return count

    '''
    @param self
    @param isConnected adjacency matrix 
    if graph[i][j] is 1, then the nodes i and j are connected
    Using an adjacency matrix is not an efficient way of getting the neighbors 
    of a node
    '''
    def build_neighbors(self, graph:list[list[int]]):
        n = len(graph[0])

        #build the adjacency list from the adjacency matrix
        for i in range(n):
            neighbors = []
            for j in range(n):
                if i != j:
                    if graph[i][j]:
                        neighbors.append(j)
            self.neighbors[i] = neighbors

    '''
    This function traverse all the neighbors associated with the given node and 
    mark them as visited.
    @param self
    @param node:int
    '''
    def dfs(self, node:int):
        if node in self.visited:
            return

        self.visited.add(node)

        for neighbor in self.getNeighbors(node):
            if neighbor not in self.visited:
                self.dfs(neighbor)

    ''' 
    This function returns the neighbors of a given node
    @param self
    @param node:int 
    '''
    def getNeighbors(self, node:int):
        return self.neighbors[node]
    
graph = [[1, 1, 0], [1,1,0], [0,0,1]]

g = Graph()
print(g.count_connected_components(graph))
