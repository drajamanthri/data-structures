from collections import defaultdict

class Graph:
    def __init__(self):
          self.neighbors:defaultdict 
          self.visited = set()

    def dfs(self, node:str):
         print(node)
         self.visited.add(node)
         for neighbor in self.neighbors[node]:
              if neighbor not in self.visited:
                   self.dfs(neighbor)
   
neighbors = defaultdict(list)
neighbors['A'] = ['C', 'D', 'B']
neighbors['B'] = ['A', 'E']
neighbors['C'] = ['A', 'E']
neighbors['D'] = ['A', 'E']
neighbors['E'] = ['D', 'B', 'C']

graph = Graph()
graph.neighbors = neighbors
graph.dfs('A')
    