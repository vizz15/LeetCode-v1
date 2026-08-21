import math
from itertools import combinations

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        
        # 1. Precompute all possible combinations of coins and their LCMs.
        # This keeps the inner binary search loop incredibly fast.
        combos = []
        n = len(coins)
        for r in range(1, n + 1):
            for combo in combinations(coins, r):
                # Calculate the collective LCM of the chosen group of coins
                current_lcm = combo[0]
                for coin in combo[1:]:
                    current_lcm = math.lcm(current_lcm, coin)
                
                # If the combination has an ODD number of coins, we ADD the count
                # If it has an EVEN number of coins, we SUBTRACT the count (to fix overlaps)
                is_odd = (r % 2 != 0)
                combos.append((current_lcm, is_odd))
        
        # 2. Helper function to count unique amounts <= mid
        def count_amounts(mid: int) -> int:
            total_count = 0
            for lcm_val, is_odd in combos:
                if is_odd:
                    total_count += mid // lcm_val
                else:
                    total_count -= mid // lcm_val
            return total_count

        # 3. Binary Search for the answer
        # Lower bound: 1
        # Upper bound: The absolute worst-case scenario (smallest coin value * k)
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # If the count of unique amounts is enough, try to find a smaller valid guess
            if count_amounts(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                # If the count is too small, we must guess a higher number
                low = mid + 1
                
        return ans

        