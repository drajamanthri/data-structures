<h1>Pair of numbers that sum to target</h1>
Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. 

<h2>Algorithm</h2>
i = pointer 1 <br>
j = pointer 2 <br>
ei = element at pointer 1<br>
ej = element at pointer 2

<ul>
<li>If the sum of ei and ej is the same as the target, we found a match</li>
<li>If the sum is less than the target, we need to decrement pointer 2</li>
<li>If the sum is greater than the target, we need to increment pointer 1</li>
</ul>

This algorithm works because the array is sorted.