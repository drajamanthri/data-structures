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
<h3>Adjacency Matrix</h3>
The graph inputs are given as an adjacency matrix. If graph[i][j] is 1, then the nodes i and j are connected. To get neighbors of a node, an adjacency matrix is not efficient. Therefore, we will pre process the adjacency matrix to build a adjacency list. 
<h3>Matrix</h3>
The graph inputs are given as a matrix. In this case, the neighbors can be access with O(1). Therefore, preprocessing is not necessary.

<h2>Complexity for adjacency matrix</h2>
n = number of nodes. <br>
We always have to build the adjacency list by iterating the n by n matrix. <br>
Time complexity = O(n^2) <br>

<br>
Memory depends on the number of nodes and the edges. <br>
Space complexity = O(n + e)

<h2>Complexity for matrix graph inputs</h2>
m * n = number of nodes. <br>
We always have to iterate the m by n matrix. <br>
Time complexity = O(m * n) <br>

<br>
Memory depends on the number of nodes and the edges. <br>
Space complexity = O(#of nodes + e)
e is a constant which is 4.<br>
Space complexity = O(m *n)

