<h1>Binary string</h1>
You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"? <br>

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
<br>

In another words, find the longest sub array which contains at most 1 0.
<br>

<h2>Algorithm</h2>
Use sliding window algorithm.<br>
<h3>Sub array criteria</h3>
Contains at most 1 zero.

<h2>Time complexity</h2>
O(n) <br>
Where n is the number of characters. <br>
The right moves at most n times and the left moves at most n times.<br>
O(2n) = O(n)<br>

<h2>Space complexity</h2>
O(1)<br>

The space taken by left, right, length, and zero counter.