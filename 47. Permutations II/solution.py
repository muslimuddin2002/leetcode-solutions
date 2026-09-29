class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort()  # Sort to easily handle duplicates
        used = [False] * len(nums)
        
        def backtrack(path: list[int]):
            if len(path) == len(nums):
                result.append(list(path))
                return
            
            for i in range(len(nums)):
                # If the element is already used, skip it
                if used[i]:
                    continue
                
                # If the current element is a duplicate of the previous one and the previous
                # one has not been used yet, skip it to avoid generating duplicate permutations
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                
                backtrack(path)
                
                path.pop()
                used[i] = False
                
        backtrack([])
        return result
