from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.neighbors:defaultdict 

    '''
    @param self
    @param target:int starting node
    @param k:int the distance
    @return list a list of nodes at distance k from the target node
    '''
    def nodes_at_distance(self, target:int, k:int)->list:
        q = deque([(target, 0)]) #(node, level)
        visited = set()
        result = []
        while q:
            node, level = q.popleft()
            if node in visited:
                continue 

            visited.add(node)
            if level == k:
                result.append(node)
            elif level > k:
                continue 

            for neighbor in self.neighbors[node]:
                if neighbor not in visited:
                    q.append((neighbor, level+1))
        return result
    
neighbors = defaultdict(list)
neighbors[3] = [5, 1]
neighbors[5] = [3, 6, 2]
neighbors[1] = [3, 0, 8]
neighbors[6] = [5]
neighbors[2] = [5, 7, 4]
neighbors[0] = [1]
neighbors[8] = [1]
neighbors[7] = [2]
neighbors[4] = [2]
graph = Graph()
graph.neighbors = neighbors
print(graph.nodes_at_distance(5, 2))