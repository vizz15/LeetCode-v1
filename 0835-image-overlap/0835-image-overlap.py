from collections import Counter

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        # 1. Collect coordinates of all '1's in both images
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Track transformation vector frequencies
        transformation_counts = Counter()
        
        # 2. Calculate shift vectors for every pair of 1s
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                # The unique translation vector needed to line up these two 1s
                shift_vector = (r2 - r1, c2 - c1)
                transformation_counts[shift_vector] += 1
                
        # 3. Return the maximum count found. If there are no 1s, return 0.
        return max(transformation_counts.values()) if transformation_counts else 0
