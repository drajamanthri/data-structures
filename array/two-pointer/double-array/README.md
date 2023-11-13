<h1>Double Array Two Pointers</h1>
In these types of algorithms, we have two pointers at the beginning of two arrays. At each iteration, we increment one or both pointers. 
<h2>Pointer movement</h2>
<h3>Pointers move always</h3>
In these types of algorithms, pointers always move on each iteration.
<br>
Example:
<code>
<pre>
    array1 = [1, 2, 3]
    array2 = [4, 5]

    i = 0
    j = 0

    while i < len(array1) and j < len(array2):
        i += 1
        j += 1

        #do something with array1[i] and array2[j]

    #at the end, one array can be not empty.
    #Therefore, exhaust the non empty array
    while i < len(array1):
        i += 1
        #do something with array1[i]

    while j < len(array2):
        j += 1
        # do something with array2[j]
</pre>
</code>
<h3>Pointers movement depends on the values at the pointers</h3>
In these types of algorithms, the pointer movement depends on the values at the pointers.
<h2>Time complexity</h2>
n: The length of array 1<br>
m: The length of array 2<br>
<br>
Time complexity = O(n + m)
<br>
This is because in the worst case, we might traverse both arrays. 
<h2>Space Complexity</h2>
Space complexity = O(1)<br>
<br>
Space taken by i and j. Assuming the space complexity of each iteration is O(1)

