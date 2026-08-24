from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Compute prefix sums of the original stones array
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stones[i]
            
        # dp will store the maximum score difference a player can get
        # from the remaining choices. We optimize space to O(1) extra variables.
        # Starting from the last possible choice point (index n - 1)
        ans = pref[n]
        
        # Iterate backwards from the second to last element to the second element
        for i in range(n - 2, 0, -1):
            ans = max(ans, pref[i + 1] - ans)
            
        return ans
