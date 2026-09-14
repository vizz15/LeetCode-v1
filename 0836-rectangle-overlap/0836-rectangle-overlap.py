class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Check if the horizontal intersection has a positive width
        x_overlap = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        
        # Check if the vertical intersection has a positive height
        y_overlap = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        
        return x_overlap and y_overlap
