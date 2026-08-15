# Time Complexity: O(4^n / n^1.5) - bounded by the nth Catalan number, which is
#                   the number of unique BSTs; each is built in O(n) time, but the
#                   dominant cost is enumerating the Catalan-many structures/combinations
# Space Complexity: O(4^n / n^1.5) - to store all generated trees (output size is
#                    Catalan number many trees), plus O(n) recursion depth

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(start: int, end: int) -> List[Optional[TreeNode]]:
            if start > end:
                return [None]

            trees = []
            for root_val in range(start, end + 1):
                left_subtrees = build(start, root_val - 1)
                right_subtrees = build(root_val + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return build(1, n)
