<h1>Two Pointer - Single array</h1>
In these types of algorithms, we place two pointers of the opposite directions of the same array.
<p>
Properties
<ul>
<li>
Two pointers can be used to traverse an array starting from the opposite ends. 
</li>
<li>
At each iteration, one or both pointers move towards each other.
</li>
<li>
Pointer move logic depends on the problem.
</li>
<li>
The traversal stops when two pointers stops. 
</li>
</ul>
</p>
<h2>Pointer movement</h2>
<h3>Pointers move always</h3>
In these types of algorithms, pointers always move on each iteration.
<br>
Example:
<code>
<pre>
a = [1, 2, 3, 4, 5]
i = 0
j = len(a) - 1

while i <= j:
    print(a[i], a[j])
    i +=1
    j -=1
</pre>
</code>
<h3>Pointer movement depends on the values at pointers</h3>
In this style of problems, pointer movement depends on the values at the pointers. How we want to compare the values at the pointers depend on the problem.

<h2>Time complexity</h2>
<p>
Time complexity = O(n)
<br>
If the complexity of each iteration is O(1)
</p>
<h2>Space complexity</h2>
<p>
Space complexity = O(1)
<br>
Space taken by two pointers is a constant.
</p>