<h1>Swap Edge Direction</h1>
<h2>Problem Definition</h2>
 There are n number of nodes (0 to n-1). <br>
 Constrains
 <ul>
    <li>Edges are directed</li>
    <li>There is only one way between any two nodes</li>
    <li>Edges are given as a list of edges. Edge = (x,y). The direction is from x to y.</li>
 </ul>
 Find how many nodes have to be swapped so that all the edges are directed to the node 0.
<h2>Algorithm</h2>
<ul>
    <li>Generate an undirected graph so that we can traverse from 0 to all the other nodes.</li>
    <li>Store the original edges so that we can decide if an edge should be swapped when traversing.</li>
    <li>Start DFS traversal from node 0. With DFS, we are always traversing away from 0. Check if (node, neighbor) exists in the original edges. If it exists, it needs to be swapped. Therefore, increment a counter.</li>
</ul>

<h2>Complexity</h2>
Time complexity = O(n) <br>
We traverse each node only once. <br>

Space Complexity = O(n) <br>
The space taken by undirected graph hash map, edges set, and visited set are proportional to n.