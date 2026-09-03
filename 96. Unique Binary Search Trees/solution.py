class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] stores the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # j is chosen as the root, so j-1 nodes go to the left subtree, 
                # and i-j nodes go to the right subtree.
                dp[i] += dp[j - 1] * dp[i - j]
                
        return dp[n]
