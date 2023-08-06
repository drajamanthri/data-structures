<h1>Binary Tree- Count matching nodes</h1>

We would want to count matching nodes based on ancestors. <br>

For example, count nodes that are greater or equal to nodes in the path from root.

<h2>Recursive implementation</h2>
<p>In the recursive implementation, the most common technique is parent passing parameters to child dfs calls and child dfs calls return the result to parent. Here children are the left sub tree and the right sub tree.</p>
<p>Following above approach, we can pass current max to child dfs calls. Then the child dfs calls return the matching node counts.</p>

<h2>Iterative implementation</h2>
There are two common methods of tracking node related data.
<ul>
    <li>Storing data in the node. Note that this does not work for graphs where node can be accessed by multiple paths. But this can be used for trees because a node has a single path. </li>
    <li>Instead of pushing the node to the stack, push a list or a tuple to the stack with data.</li>
</ul>
For this solution, lets use pushing a tuple.

<h2>Space and time complexity</h2>
These are the worst case complexities.<br>
n = number of nodes<br>
Time complexity = O(n)<br>
Space complexity = O(n)