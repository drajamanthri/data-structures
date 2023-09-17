<h1>Nodes at distance k</h1>
Given the target (starting node) and k distance, find all the nodes at distance k.<br>

Graph is given by an adjacency list.

<h2>Algorithm</h2>
Here we assume that the graph is given by an adjacency list. If the graph is given as a list of edges or adjacency matrix, it would have to be converted to an adjacency list so that we can access the neighbors of any node with the time complexity of O(1).
<br>
<br>
To analyze nodes at radius k, the most appropriate algorithm is BFS. Start BFS traversal from the target node. Keep track of the level. when the level is equal to k, add it to the result list.
<h2>Complexity</h2>
The complexity is the same as BFS.<br>
Time complexity = O(n+e) <br>
Space complexity = O(n) 