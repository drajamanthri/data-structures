class Graph:
    def __init__(self):
        self.grid:list[list[int]]
        self.m:int #number of rows
        self.n:int #number of columns
        self.diffs = [
            (0, -1), 
            (-1, 0), (1, 0),
            (0, 1)
        ]
        

    '''
    This function counts the number of connected components of the given graph.
    @param self
    @param grid:list[list[int]] graph as a matrix
    @return int number of connected components
    '''
    def count(self, grid:list[list[int]])->int:
        if len(grid) == 0:
            return 0
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 1:
                    count += 1
                    self.dfs((i, j))

        return count

    '''
    This function traverse the neighbors of the given node and mark
    grid[i][j] = 1
    @param self
    @param node:tuple (i, j)
    '''
    def dfs(self, node:tuple):
        node_i, node_j = node 
        
        if self.grid[node_i][node_j] == 0:
            return
        
        self.grid[node_i][node_j] = 0

        for neighbor_i, neighbor_j in self.neighbors(node):

            if self.grid[neighbor_i][neighbor_j] == 1:
                self.dfs((neighbor_i, neighbor_j))

    '''
    @param self
    @param node:tuple The coordinates of the node (i, j) 
    @return list[tuple] list of neighbors
    Assume that the neighbors are only the horizontal and vertical 
    adjacent cells.
    '''
    def neighbors(self, node:tuple) -> list[tuple]:
        node_i, node_j = node
        result = []
        for di, dj in self.diffs:
            i = node_i + di
            j = node_j + dj 
            if 0 <= i < self.m and 0 <= j < self.n:
                if self.grid[i][j] == 1:
                    result.append((i, j))

        return result
    
graph = Graph()
grid = [
    [1, 1, 0, 0, 0], 
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

count = graph.count(grid)
print(count)