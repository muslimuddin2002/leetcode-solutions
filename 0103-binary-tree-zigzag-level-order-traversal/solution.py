# Time Complexity: O(n) - each node is visited exactly once
# Space Complexity: O(n) - the queue can hold up to one full level of nodes at worst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque([root])
        left_to_right = True
        while queue:
            cur_level_res = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level_res.append(node.val)
            if not left_to_right:
                cur_level_res.reverse()
            res.append(cur_level_res)
            left_to_right = not left_to_right
        return res
