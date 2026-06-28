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

        def dfs(node, current_path):
            if node:
                current_path.append(str(node.val))

                if not node.left and not node.right:
                    paths.append("->".join (current_path))
                else:
                    if node.left:
                        dfs(node.left,list(current_path))
                    if node.right:
                        dfs(node.right,list(current_path))

        dfs(root,[])
        return paths
        