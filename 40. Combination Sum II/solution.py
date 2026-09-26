class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []
        candidates.sort()  # Sort to easily handle duplicates and stop early
        
        def backtrack(remain: int, path: list[int], start: int):
            if remain == 0:
                result.append(list(path))
                return
            if remain < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicate elements at the same tree level to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # If current candidate exceeds the remaining target, no need to continue (since sorted)
                if candidates[i] > remain:
                    break
                    
                path.append(candidates[i])
                backtrack(remain - candidates[i], path, i + 1)  # Each number can only be used once, so move to i + 1
                path.pop()
                
        backtrack(target, [], 0)
        return result
