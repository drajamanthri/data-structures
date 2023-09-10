<h1>Zero In-degree</h1>
In-degree is the # of incoming edges. 
<h2>Problem Definition</h2>
 There are n number of nodes (0 to n-1). Find the nodes with 0 in-degree.<br>
 Constrains
 <ul>
    <li>Edges are directed</li>
    <li>Graph is acyclic</li>
    <li>Input is given as edges. edge = [x, y]. The direction is from x to y.</li>
 </ul>

<h2>Algorithm</h2>
<ul>
    <li>Generate a map of nodes and their in-degree</li>
    <li>For each node, check if it exist in the map.</li>
</ul>

<h2>Complexity</h2>
Time complexity = O(n + e) <br>
We have to iterate edges to build the map then nodes to find the nodes with 0 in-degree.<br>

Space Complexity = O(n) <br>
We need n spaces to store the in-degrees of each node.