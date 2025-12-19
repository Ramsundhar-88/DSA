# Given an array of integers nums, return the value of the largest element in the array


class Solution:
    def largestElement(self, nums):
        largest = nums[0]        
        for num in nums:            
            if num > largest:
                largest = num
        return largest

sol = Solution()
print(sol.largestElement([3, 3, 6, 1]))       
print(sol.largestElement([3, 3, 0, 99, -40])) 
