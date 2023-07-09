from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.neighbors:defaultdict

    def bfs(self, root:str):
        visited = set()
        queue = deque()

        #add the root node to the queue
        queue.append(root)
        while queue:
            #read the node at the front of the queue
            node = queue.popleft()
            if node in visited:
                continue

            visited.add(node)
            print(node)
            for neighbor in self.neighbors[node]:
                if neighbor not in visited:
                    #add un-visited neighbors to the queue
                    queue.append(neighbor)

graph = Graph()
graph.neighbors = defaultdict(list)
graph.neighbors['A'] = ['B', 'C', 'D']
graph.neighbors['B'] = ['A', 'E']
graph.neighbors['C'] = ['A', 'E']
graph.neighbors['D'] = ['A', 'E']
graph.neighbors['E'] = ['B', 'C', 'D']

graph.bfs('A')
