<h1>Sliding window</h1>
<h2>Sub array</h2>
Sub array is a contiguous section of an array. <br>

Example<br>
<code>
array: [2, 4, 5, 10] <br>
Sub arrays: <br>
[2, 4] <br>
[4, 5, 10]
</code>

<h2>Sliding window problem properties</h2>
<ul>
    <li>Define criteria of sub array</li>
    <li>Ask to find the sub array</li>
</ul>
<br>

<h2>Two pointer Vs Sliding Window</h2>
Two pointer problems are interested in the two elements pointed by the two pointers.<br>

Sliding window problem interested in all the elements between two pointers.

<h2>Algorithm</h2>
<ul>
    <li>start from left = right =0</li>
    <li>Expand the window (move right to the right) until the constraint on the sub array is broken</li>
    <li>Shrink the window from the left until the constraint on the sub array is valid again</li>
    <li>Repeat expanding and shrinking</li>
</ul>

<code>
<pre>
def fn(arr):
    left = 0
    for right in range(len(arr)):
        Add element at arr[right] to window

        while window is invalid:
            Remove element at arr[left] from window

        Here we always have a valid window
        Update answer
</pre>
</code>
<h2>Time complexity</h2>
O(2n)<br>
Right can move n times and the left can move n times.<br>
<code>
O(n)
</code>