from collections import deque

class Graph:
    def __init__(self):
        self.graph:list(list(int))
        self.visited:set
        self.nb_diffs = [(0, -1), (0, 1), (-1, 0), (1,0)]
        self.m:int
        self.n:int

    '''
    This function find the distance to the closest 0 for each cell.
    @return list[list[int]]
    '''
    def find_distance(self)-> [[int]]:
        self.visited = set()
        self.m = len(self.graph)
        self.n = len(self.graph[0])
        
        q = deque()
        #first add all the 0s to the queue
        for i in range(self.m):
            for j in range(self.n):
                if self.graph[i][j] == 0:
                    q.append((i,j,0)) #(i, j, distance)

        #dfs starting from 0s
        while(q):
            i, j, d = q.popleft() #d = the distance to node i,j form the closest 0
            if (i,j) in self.visited:
                continue 
            #record the distance from the closest 0
            self.graph[i][j] = d 
            self.visited.add((i,j))
            #add the neighbors to the queue
            nbd = d + 1

            for nbi, nbj in self.neighbors((i,j)):
                if (nbi, nbj) not in self.visited:
                    q.append((nbi, nbj, nbd))

        return self.graph

    '''
    @param self
    @param v:tuple (i, j) where i = row and j = column
    @return a list of neighbors of the given node
    '''
    def neighbors(self, v:tuple)->list[tuple]:
        i, j = v
        neighbors = []
        for di, dj in self.nb_diffs:
            nbi = i + di 
            nbj = j + dj 
            if 0 <= nbi < self.m and 0 <= nbj < self.n:
                neighbors.append((nbi, nbj))

        return neighbors

data = [[0,0,0],
        [0,1,0],
        [1,1,1]]

graph = Graph()
graph.graph = data
print(graph.find_distance())