class Solution:
    '''
    Given a string of ones and zeros, this function finds the length of
    the longest sub array which contains at most 1 zero.
    '''
    def solve(self, s:str)->int:

        left = length = zeros =0

        for right in range(len(s)):
            if s[right] == '0':
                zeros += 1

            while zeros > 1:
                #while the window is invalid, shrink the left
                #invalid = sub array contains more than 1 zeros
                if s[left] == '0':
                    zeros -= 1
                    left += 1
                else:
                    left += 1

            #here, the sub array must be valid
            #valid = sub array contains at most 1 zero
            #calculate the length
            length = max (length, right - left + 1)

        return length
    
solution = Solution()
s = '1101100111'

result = solution.solve(s)
print(result)