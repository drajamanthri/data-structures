class Solution:
    '''
    This function find the largest sum of the sub array with size k
    '''
    def solve(self, arr:list, k:int)->int:
        current_result = 0

        #initialize the window
        for i in range(k):
            current_result += arr[i]

        result = current_result

        #test the other possible windows
        for right in range(k, len(arr)):
            #add the right element to the window
            current_result += arr[k]
            #remove the left element from the window
            current_result -= arr[k-1]
            #update the result
            result = max(current_result, result)

        return result
    
solution = Solution()
arr = [3, -1, 4, 12, -8, 5, 6]
result = solution.solve(arr, 4)
print(result)
        