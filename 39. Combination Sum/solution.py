class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        
        def backtrack(remain: int, path: list[int], start: int):
            if remain == 0:
                result.append(list(path))
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # Since we can reuse the same element, we pass 'i' instead of 'i + 1'
                backtrack(remain - candidates[i], path, i)
                path.pop()
                
        backtrack(target, [], 0)
        return result
