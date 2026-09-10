# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matching_nodes = 0
        
        def traverse(node):
            if not node:
                # Base case: return (sum = 0, count = 0)
                return 0, 0
            
            # Post-order traversal: collect info from children
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            
            # Calculate current node's subtree sum and count
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Calculate floor average (integer division handles rounding down automatically)
            subtree_average = current_sum // current_count
            
            # Check if current node value equals the average
            if node.val == subtree_average:
                self.matching_nodes += 1
                
            return current_sum, current_count
            
        traverse(root)
        return self.matching_nodes
