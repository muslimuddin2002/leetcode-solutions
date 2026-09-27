class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        
        def backtrack(path: list[int], used: list[bool]):
            if len(path) == len(nums):
                result.append(list(path))
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # Choose the element
                used[i] = True
                path.append(nums[i])
                
                # Explore
                backtrack(path, used)
                
                # Un-choose (backtrack)
                path.pop()
                used[i] = False
                
        backtrack([], [False] * len(nums))
        return result
