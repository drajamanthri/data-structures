'''
Traversing an array starting at both ends.
'''
a = [1, 2, 3, 4, 5]
i = 0
j = len(a) - 1

while i <= j:
    print(a[i], a[j])
    i +=1
    j -=1

