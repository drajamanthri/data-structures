from collections import defaultdict

class Graph:
    def __init__(self):
          self.neighbors:defaultdict 

    def dfs(self, node:str):
         pass
   
neighbors = defaultdict(list)
neighbors['A'] = ['C', 'D', 'B']
neighbors['B'] = ['A', 'E']
neighbors['C'] = ['A', 'E']
neighbors['D'] = ['A', 'E']
neighbors['E'] = ['D', 'B', 'C']

graph = Graph()
graph.neighbors = neighbors

    