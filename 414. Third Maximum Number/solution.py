class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        # Use a set to get distinct numbers
        distinct_nums = set(nums)
        
        # If there are less than 3 distinct numbers, return the maximum
        if len(distinct_nums) < 3:
            return max(distinct_nums)
            
        # Otherwise, remove the maximum twice to find the third maximum
        distinct_nums.remove(max(distinct_nums))
        distinct_nums.remove(max(distinct_nums))
        
        return max(distinct_nums)
