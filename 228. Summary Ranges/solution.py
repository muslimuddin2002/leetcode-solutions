class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
            
        result = []
        start = nums[0]
        
        for i in range(len(nums)):
            # Check if it's the last element or if the next element breaks the consecutive sequence
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i]}")
                
                # If not the last element, update start for the next range
                if i < len(nums) - 1:
                    start = nums[i + 1]
                    
        return result
