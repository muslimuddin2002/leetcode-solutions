class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        current_val = None
        current_count = 0
        max_count = 0
        modes = []
        
        def inorder(node):
            nonlocal current_val, current_count, max_count, modes
            if not node:
                return
            
            inorder(node.left)
            
            # বর্তমান নোডের মান প্রসেস করা
            if node.val == current_val:
                current_count += 1
            else:
                current_val = node.val
                current_count = 1
                
            if current_count > max_count:
                max_count = current_count
                modes = [current_val]
            elif current_count == max_count:
                modes.append(current_val)
                
            inorder(node.right)
            
        inorder(root)
        return modes
