from collections import defaultdict 

class Graph:
    def __init__(self):
        self.neighbors:defaultdict

    def dfs(self, start):
        stack = [start]
        visited = set()
        
        while stack:
            #visit the top element of the stack
            node = stack.pop()
            #if the node is visited, ignore it.
            if node in visited:
                continue

            print(node)
            visited.add(node)
            for neighbor in self.neighbors[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = Graph()
neighbors = defaultdict()
#test with different neighbor configurations
neighbors['A'] = ['B', 'C', 'D']
neighbors['B'] = ['A', 'C', 'E']
neighbors['C'] = ['A', 'B', 'E']
neighbors['D'] = ['A', 'E']
neighbors['E'] = ['B', 'C', 'D']
graph.neighbors= neighbors
graph.dfs('A')