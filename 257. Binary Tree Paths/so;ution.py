class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result = []
        
        def dfs(node, current_path):
            if not node:
                return
            path = current_path + str(node.val)
            if not node.left and not node.right:
                result.append(path)
                return
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")
                
        dfs(root, "")
        return result
