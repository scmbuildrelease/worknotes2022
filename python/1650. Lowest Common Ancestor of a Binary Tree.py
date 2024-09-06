#1650. Lowest Common Ancestor of a Binary Tree

class Node:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Start from both nodes
        a, b = p, q
        
        # Traverse upwards from both p and q
        while a != b:
            # If a reaches the root, switch to q
            a = a.parent if a else q
            # If b reaches the root, switch to p
            b = b.parent if b else p
        
        # When they meet, that's the LCA
        return a
