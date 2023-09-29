<h1>Closest 0</h1>
<p>
Given an m by n matrix with 0s and 1s, for each cell, find the nearest 0
</p>

<p>For cells with 0, the distance to the nearest 0 is 0.</p>

<h2>Algorithm</h2>
<p>One approach is to start BFS from 1. This is inefficient because for each 1, we need to BFS traverse all the rest of the vertices.</p>

<p>The efficient approach is to start BFS traversal from 0s. With this method, every node is visited only onces by the closest 0. Therefore, we can mark each visited node as visited and record it's distance.</p>
<h2>Complexity</h2>
The complexity is the same as BFS.<br>
Time complexity = O(number of nodes) = O(m*n) <br>
Space complexity = O(number of nodes) = O(m*n). To keep track of visited. 