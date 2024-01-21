<h1>Sub array count</h1>
Valid sub array count can be calculated as follows, <br>

<code>
<pre>
if window is valid:
    length = right - left + 1
    if length > 0:
        count += length
</pre>
</code>
where<br>
length = current window length<br>
count = current number of valid sub arrays 