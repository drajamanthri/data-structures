<h1>Sliding window - fixed window</h1>
If the window size is fixed, when we add an element to the right, we need to remove an element from the left. <br>

<h2>Algorithm</h2>

<code>
<pre>
def fn (arr, k):
    current_result = 0
    result = 0

    for i in range(k):
        initialize the window
        build current result

    initialize result
    ex result = current_result

    for i in range(k, len(arr)):
        #i is the right. i - k is the left
        #add right element to the window
        #remove the left element from the window
        #update answer

    return result

</pre>
</code>