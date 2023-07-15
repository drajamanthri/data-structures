from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.neighbors:defaultdict

    '''
    This function returns the shortest path from start to the end node
    using bfs
    @param self
    @param start: Starting node
    @param end: Ending node
    @return the shortest path
    '''
    def shortest_path(self, start:str, end:str)->list:
        visited = set()
        queue = deque()
        queue.append([start])

        while queue:
            path = queue.popleft()
            node = self.get_current_node_from_path(path)
            if node == end:
                #if the node equals the destination, we found the shortest path 
                # return the path
                return path 
            
            if node not in visited:
                visited.add(node)
                for neighbor in self.neighbors[node]:
                    neighbor_path = list(path)
                    neighbor_path.append(neighbor)
                    queue.append(neighbor_path)


    '''
    In the path the last element is the current node
    @param self
    @param path: path to the current node
    @return The current node
    '''
    def get_current_node_from_path(self, path:list)->str:
        if len(path) > 0:
            return path[len(path) - 1]
        else:
            return ''

'''
Initialize the graph and the neighbors for testing the algorithm.
'''
graph = Graph()
neighbors = defaultdict(list)
neighbors['A'] = ['C', 'D', 'B']
neighbors['B'] = ['A', 'E']
neighbors['C'] = ['A', 'D', 'E']
neighbors['D'] = ['A', 'C', 'E']
neighbors['E'] = ['B', 'D', 'C']
graph.neighbors = neighbors
print(graph.shortest_path('A', 'E'))