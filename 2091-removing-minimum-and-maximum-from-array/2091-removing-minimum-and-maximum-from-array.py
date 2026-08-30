class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
            
        # 1. Find indices of max and min elements
        max_idx = nums.index(max(nums))
        min_idx = nums.index(min(nums))
        
        # 2. Identify which index comes first and which comes second
        first_idx = min(max_idx, min_idx)
        second_idx = max(max_idx, min_idx)
        
        # Scenario 1: Delete both from the front (left side)
        # We must go all the way to the second index.
        from_front = second_idx + 1
        
        # Scenario 2: Delete both from the back (right side)
        # We must go from the end all the way down to the first index.
        from_back = n - first_idx
        
        # Scenario 3: Delete the first one from front, second one from back
        # Left side takes (first_idx + 1) deletions. Right side takes (n - second_idx) deletions.
        from_both = (first_idx + 1) + (n - second_idx)
        
        # The answer is simply the absolute minimum cost among all three scenarios
        return min(from_front, from_back, from_both)
