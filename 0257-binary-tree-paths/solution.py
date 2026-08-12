# Time Complexity: O(n^2) - each node is visited once, but building the path string at each leaf can take O(n) in the worst case (skewed tree), leading to O(n^2) overall
# Space Complexity: O(n^2) - storing up to n paths, each up to O(n) length in the worst case

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []

        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)

        dfs(root, "")
        return paths
