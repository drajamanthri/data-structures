class Solution:
    def solve(self, nums: list[int], k: int) -> int:
        left = count = 0
        product = 1

        for right in range(len(nums)):
            product = product * nums[right]

            while product >= k and left < len(nums):
                product = product /nums[left]
                left += 1

            if product < k:
                length = right - left + 1
                if length > 0:
                    count += length

        return count
    
solution = Solution()
arr = [10,5,2,6]
result = solution.solve(arr, 100)
print(result)
