# Time Complexity: O(n^2) - each node is visited once (O(n)), but copying the path list at each valid leaf can take O(n) in the worst case
# Space Complexity: O(n^2) - storing up to n paths, each up to O(n) length in the worst case; plus O(h) recursion stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(node, remaining):
            if not node:
                return

            path.append(node.val)
            remaining -= node.val

            if not node. left and not node. right and remaining == 0:
                res.append(path[:])
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)

            path.pop()

        dfs(root, targetSum)
        return res
