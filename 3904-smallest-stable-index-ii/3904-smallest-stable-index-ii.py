class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
            
        # 1. Precompute Prefix Maximums
        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], nums[i])
            
        # 2. Precompute Suffix Minimums
        suff_min = [0] * n
        suff_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])
            
        # 3. Find the first index that satisfies the stability condition
        for i in range(n):
            if pref_max[i] - suff_min[i] <= k:
                return i
                
        return -1
