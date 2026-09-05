# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, p, q):
        if p == None and q == None:
            return True
        if (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False
        elif p.val == q.val:
            if self.sameTree(p.left, q.left) == False:
                return False
            if self.sameTree(p.right, q.right) == False:
                return False

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot):
            return True
        if not root:
            return False
        
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):return True
        
        return False
        