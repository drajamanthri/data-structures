<h1>Shortest path between two nodes.</h1>
To find the shortest path between two nodes, we use the breath first search algorithm.

<h2>Algorithm</h2>
<ul>
    <li>In breath first search traversal, we traverse all the nodes of the same level before traversing the nodes of the next level. Therefore, the breath first search algorithm is perfect for finding the shortest path.</li>
    <li>The first time we reach the destination node, traversal is completed. And, the path is the shortest path.</li>
</ul>

<h2>Time complexity</h2>
n: number of nodes
e: number of edges
Time complexity = O(n + e)

In the worst case, we need to traverse all the nodes and iterate all the edges.

<h2>Space Complexity</h2>

Space complexity = O(n)
In the worst case, the depth is 1 and we need to queue all the nodes.