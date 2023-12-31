<h1>Traverse all the vertices with DFS</h1>
<img src="images/graph.png">

<h2>Algorithm</h2>
<ul>
    <li>Because we are using the depth first search algorithm, for each neighbor, we need to traverse as deep as we can go, before going to the next neighbor.</li>
    <li>DFS can be implemented by using recursion or stack. In this solution, we will be using recursion. </li>
    <li>A vertex should not be traversed more than once. To prevent infinite loops, we'll be using a set which tracks the visited vertices.</li>
</ul>

<h2>Time complexity</h2>
n = number of nodes
e = number of edges

Time complexity = O(n + e)
Because we need to visit all the nodes and iterate all the edges.

<h2>Space Complexity</h2>
Space complexity = O(n)
In the worst case, the graph is a line and all the nodes has to be stored in the
stack.