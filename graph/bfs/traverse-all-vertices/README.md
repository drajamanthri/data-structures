<h1>Traverse all the vertices with BFS</h1>
<img src="images/graph.png">

<h2>Algorithm</h2>
<ul>
    <li>Because we are using the breadth first search algorithm, for each node, we need to visit all the immediate neighbors before traversing the neighbors of the next level. In BFS, traversal is done level by level.</li>
    <li>BFS is implemented by using a queue data structure. All the nodes of a certain level are in front of the queue.</li>
    <li>A vertex shold not be visited more than once. To prevent infinite loops, we'll be using a set which tracks the visited verticies.</li>
</ul>

<h2>Time complexity</h2>
n = number of nodes
e = number of edges

Time complexity = O(n + e) <br/>
Because we need to visit all the nodes and iterate all the edges.

<h2>Space Complexity</h2>
Space complexity = O(n)<br/>
The space need for the queue is at most n.<br/>
The space need to store the visited nodes is n.
