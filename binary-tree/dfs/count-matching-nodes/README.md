<h1>Binary Tree- Count matching nodes</h1>

We would want to count matching nodes based on ancestors. <br>

For example, count nodes that are greater or equal to nodes in the path from root.

<h2>Recursive implementation</h2>
<p>In the recursive implementation, the most common technique is parent passing parameters to child dfs calls and child dfs calls return the result to parent.</p>
<p>Following above approach, we can pass current max to child dfs calls. Then the child dfs calls return the matching node counts.</p>

<h2>Space and time complexity</h2>
These are the worst case complexities.<br>
n = number of nodes<br>
Time complexity = O(n)<br>
Space complexity = O(n)