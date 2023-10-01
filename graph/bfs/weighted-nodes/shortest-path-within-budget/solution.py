from collections import deque

class Graph:
    def __init__(self):
        self.matrix:list[list[int]]
        self.m:int
        self.n:int 
        self.diffs:list[tuple] = [(-1,0), (1,0),
                                  (0, -1), (0,1)]
    '''
    @param budget:int The traversal should be within this budget.
    @return int number of minimum steps needed to traverse from (0,0) node
    to (m-1, n-1) node with the given budget
    '''
    def min_steps(self, budget:int)->int:
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])

        visited = set()

        q = deque()
        #cost of 0,0 is always 0
        q.append((0,0,0, 0)) #i, j, cost, steps

        while (q):
            i, j, cost, steps = q.popleft()
            if (i, j, cost) in visited:
                continue

            visited.add((i, j, cost))
            if i == self.m-1 and j == self.n-1:
                #if the destination node (m-1, n-1) is reached
                #return the # of steps
                return steps 
             
            for nbi, nbj in self.nbs(i,j):
                nb_cost = cost + self.matrix[nbi][nbj]
                if (nbi, nbj, nb_cost) not in visited and nb_cost <= budget:
                    q.append((nbi, nbj, nb_cost, steps+1))

        return -1
    
    def nbs(self, i, j)->list[tuple]:
        nbs = []
        for di, dj in self.diffs:
            nbi = i + di 
            nbj = j + dj

            if 0 <= nbi < self.m and 0 <= nbj < self.n:
                nbs.append((nbi, nbj))

        return nbs
    
matrix = [[0, 0, 0], 
          [3, 2, 0],
          [0, 0, 0],
          [0, 1, 3],
          [0, 0, 0]
          ]

graph = Graph()
graph.matrix = matrix
print(graph.min_steps(2))