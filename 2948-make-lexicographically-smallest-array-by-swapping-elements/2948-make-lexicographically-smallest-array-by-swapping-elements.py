class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # 1. Pair each value with its original index and sort by value
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        
        ans = [0] * n
        
        # 2. Use a two-pointer approach to find swappable groups
        i = 0
        while i < n:
            j = i + 1
            # Expand group if the difference between adjacent sorted numbers is within limit
            while j < n and sorted_pairs[j][0] - sorted_pairs[j-1][0] <= limit:
                j += 1
                
            # Current group spans from index i to j-1
            # Extract and sort the original indices of this group
            indices = sorted(sorted_pairs[k][1] for k in range(i, j))
            
            # Place the sorted values into the sorted original indices
            for k in range(i, j):
                val = sorted_pairs[k][0]
                target_idx = indices[k - i]
                ans[target_idx] = val
                
            # Move onto the next group
            i = j
            
        return ans
