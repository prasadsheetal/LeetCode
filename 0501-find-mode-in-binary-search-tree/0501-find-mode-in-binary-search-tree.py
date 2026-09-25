# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> list[int]:
        modes = []
        prev_val = None
        curr_count = 0
        max_count = 0

        def in_order(node: TreeNode) -> None:
            nonlocal prev_val, curr_count, max_count, modes
            if not node:
                return

            in_order(node.left)

            # Process current node
            if node.val == prev_val:
                curr_count += 1
            else:
                curr_count = 1
                prev_val = node.val

            if curr_count > max_count:
                max_count = curr_count
                modes = [node.val]  # Reset modes array with new maximum frequency
            elif curr_count == max_count:
                modes.append(node.val)  # Append tied mode

            in_order(node.right)

        in_order(root)
        return modes