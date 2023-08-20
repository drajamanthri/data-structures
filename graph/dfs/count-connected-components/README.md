<h1>Count connected components</h1>
Write a program to count the connected components of a given graph.

<h2>Connected Component</h2>
In a graph, nodes that are connected directly or indirectly is considered a single connected component.
<h2>Algorithm</h2>
<ul>
    <li>
        For each unvisited node
        <ul>
            <li>increment the component count</li>
            <li>traverse all the neighbors and mark them as visited</li>
        </ul>
    </li>
</ul>
In this problem, the graph inputs are given as an adjacency matrix. If graph[i][j] is 1, then the nodes i and j are connected. To get neighbors of a node, an adjacency matrix is not efficient. Therefore, we will pre process the adjacency matrix to build a adjacency list. 
<h2>Complexity</h2>
n = number of nodes. <br>
We always have to build the adjacency list by iterating the n by n matrix. <br>
Time complexity = O(n^2) <br>

<br>
Memory depends on the number of nodes and the edges. <br>
Space complexity = O(n + e)

