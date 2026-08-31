# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        # We need at least 3 nodes to have a critical point
        if not head or not head.next or not head.next.next:
            return [-1, -1]
            
        prev = head
        curr = head.next
        
        first_cp = -1
        prev_cp = -1
        
        min_dist = float('inf')
        max_dist = -1
        
        curr_idx = 1 # index of 'curr' node
        
        while curr.next:
            # Check if current node is a local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > curr.next.val
            is_minima = curr.val < prev.val and curr.val < curr.next.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    # This is our very first critical point
                    first_cp = curr_idx
                else:
                    # Update minimum distance with the adjacent pair difference
                    min_dist = min(min_dist, curr_idx - prev_cp)
                    # Update maximum distance (always from the first critical point to the current one)
                    max_dist = curr_idx - first_cp
                    
                prev_cp = curr_idx # Update previous critical point tracker
                
            # Move pointers forward
            prev = curr
            curr = curr.next
            curr_idx += 1
            
        # If we found fewer than two critical points, return [-1, -1]
        if max_dist == -1:
            return [-1, -1]
            
        return [min_dist, max_dist]

        