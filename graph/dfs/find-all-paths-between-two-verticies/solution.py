from collections import defaultdict

class Graph:
      def __init__(self):
            self.neighbors:defaultdict 
            self.paths = []
            self.visited = set()
            self.destination:str

      def dfs(self, path:list):
            node = path[len(path) - 1]
            if node == self.destination:
                  #if the destination node is found, add the path.
                  #We don't want the destination node marked as visited because there could be another path to it.
                  self.paths.append(path)
            else:
                  self.visited.add(node)
                  #if the node is not the destination, traverse all the un-visited neighbors
                  for neighbor in self.neighbors[node]:
                        if neighbor not in self.visited:
                              neighbor_path = list(path)
                              neighbor_path.append(neighbor)
                              self.dfs(neighbor_path)
                  #after traversing all the neighbors, mark the node as un-visited because there could be another path via this node
                  self.visited.remove(node)
               
   
neighbors = defaultdict(list)
neighbors['A'] = ['C', 'D', 'B']
neighbors['B'] = ['A', 'D', 'E']
neighbors['C'] = ['A', 'E']
neighbors['D'] = ['A', 'B', 'E']
neighbors['E'] = ['D', 'B', 'C']

graph = Graph()
graph.neighbors = neighbors
graph.destination = 'E'
graph.dfs('A')
print(graph.paths)

    