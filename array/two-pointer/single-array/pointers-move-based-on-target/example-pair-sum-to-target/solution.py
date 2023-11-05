
'''
Given a sorted array of unique integers and a target integer, 
return true if there exists a pair of numbers that sum to target, 
false otherwise.
parameters
----------
a: list
    list of sorted numbers
target: integer
    see the return value for more information about the targe.

Returns
-------
boolean
    True if there is 2 numbers that sums to the target.
'''
def search(a:list, target:int)->bool:
    i = 0
    j = len(a) - 1
    while i < j:
        sum = a[i] + a[j]
        if sum == target:
            return True 
        elif sum < target:
            i = i + 1
        else:
            j = j - 1
    return False 

nums = [1, 2, 4, 6, 8, 9, 14, 15]
result = search(nums, 17)
print(result)