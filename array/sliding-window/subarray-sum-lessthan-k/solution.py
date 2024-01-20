class Solution:
    def solve(self, arr:list, k:int)->int:
        left = sum = length = 0

        for right in range(len(arr)):
            #expanding
            #add right element to the window
            sum += arr[right]

            if sum > k:
                #if the sub array in invalid, shrink from the left
                sum -= arr[left]
                left += 1

            #here sub array is valid. 
            #therefore, update the length
            length = max(length, right - left + 1)

        return length
    
arr = [1, 2, 3, 1, 4]
s = Solution()
result = s.solve(arr, 3)
print(result)