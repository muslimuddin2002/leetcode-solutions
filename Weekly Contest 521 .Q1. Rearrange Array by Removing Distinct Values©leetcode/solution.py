from collections import Counter

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # Count the frequency of each number
        count = Counter(nums)
        ans = []
        
        # Continue until all elements are processed
        while count:
            # Get all distinct values currently present, sorted in ascending order
            distinct_vals = sorted(count.keys())
            
            for val in distinct_vals:
                ans.append(val)
                count[val] -= 1
                # If the count drops to zero, remove it from the counter
                if count[val] == 0:
                    del count[val]
                    
        return ans
