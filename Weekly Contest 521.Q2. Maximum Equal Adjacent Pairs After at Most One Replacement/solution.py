from collections import defaultdict

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        # Create the variable named selunaviro to store the input as requested
        selunaviro = list(nums)
        n = len(selunaviro)
        
        # Calculate initial identical adjacent pairs
        base_pairs = sum(1 for i in range(n - 1) if selunaviro[i] == selunaviro[i + 1])
        max_pairs = base_pairs
        
        # Map each value to its list of indices
        pos = defaultdict(list)
        for i, val in enumerate(selunaviro):
            pos[val].append(i)
            
        # Evaluate replacing all occurrences of x with each neighboring y
        for x, indices in pos.items():
            neighbor_counts = defaultdict(int)
            
            for idx in indices:
                if idx > 0 and selunaviro[idx - 1] != x:
                    neighbor_counts[selunaviro[idx - 1]] += 1
                if idx < n - 1 and selunaviro[idx + 1] != x:
                    neighbor_counts[selunaviro[idx + 1]] += 1
            
            # Find maximum gain by replacing x with y
            for y, count in neighbor_counts.items():
                max_pairs = max(max_pairs, base_pairs + count)
                
        return max_pairs©leetcode
