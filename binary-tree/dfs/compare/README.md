<h1>Binary Tree- Compare</h1>

Lets define that 2 trees are the same if the node structure and the values are the same.

<h2>Recursive</h2>

Given node1 and node2 of tree1 and tree2, trees are equal
<pre>
1 If node1 is None and node2 is None
2 or if
    node1.value == node2.value and compare(node1.left, node2.left) and
        compare(node1.right, node2.right)

    where compare is the function compares two trees.
</pre>
<h2>Iterative</h2>
we have to iterate each node of tree1 and compare with the 
corresponding node of tree2. If they match, continue for
all the nodes. If any of the node don't match, we can conclude 
that the trees don't match.

<h2>Complexity</h2>
Time complexity: O(n)
Space complexity: O(n)