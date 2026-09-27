"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            curr = stack.pop()
            res.append(curr.val)

            for i in range(len(curr.children)-1,-1,-1):
                stack.append(curr.children[i])
        
        return res

        