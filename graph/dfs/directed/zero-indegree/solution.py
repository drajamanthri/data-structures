class Graph:
    '''
    @param self
    @param n:int number of nodes
    @param edges [[x, y], ..]
    @return list a list of nodes with zero indegree
    '''
    def nodes_with_zero_indegree(self, n:int, edges:list[list[int]])->list:
        #calculate indgrees
        indegree = [0] * n 
        for x,y in edges:
            indegree[y] += 1

        result = []
        for node in range(n):
            if indegree[node] == 0:
                result.append(node)

        return result
    
#test with different inputs
graph = Graph()
edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
n = 6
print(graph.nodes_with_zero_indegree(n, edges))