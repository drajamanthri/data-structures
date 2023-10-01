<h1>Shortest path within budget</h1>
<p>
Given an m by n matrix with weighted nodes, find the shortest path from (0,0) node to (m-1, n-1) node within budget. Each cell of the matrix contains the weight/cost of the node. Budget is also given. Note that we are not looking for a path with the minimum cost. We are looking for the shortest path which can be achieved within the budget. If there is no such path, return -1.
</p>
<p>Assume the cost of (0,0) is always 0.</p>
<p>As the result, we can return the path or the number of steps. In this problem, we'll return the number of steps.</p>

<h2>Algorithm</h2>
<p>From (0,0) to (m-1, n-1), BFS traverse. During the traversal, we need to track the following
<ul>
    <li>node cost per path. Note that the node cost depends on the path. A node should be traversed, only if it is within budget.</li>
    <li>Number of steps.</li>
    <li>visited nodes. The visited nodes should be traversed by i, j, and cost. A node can be visited multiple times if it has a different cost via another path. In general GFS, state depends completely on a node. But in this problem, state depends on node and cost.</li>
</ul>
</p>

<h2>Complexity</h2>
<p>
The graph is a matrix. Each node has a fixed number of neighbors. Therefore at each node, the time complexity to access neighbors is a constant. We'll define it as O(1).
</p>
<p>The time complexity of BFS for matrix is O(m*n) because we traverse a single node only once. In this problem, the time complexity depends on the number of states which in m*n*budget. </p>
<p>Time complexity = O(m*n*budget)</p>
<p>The space complexity depends on the size of visited which also depends on the number of states.</p>
<p>Space complexity = O(m*n*budget)</p>