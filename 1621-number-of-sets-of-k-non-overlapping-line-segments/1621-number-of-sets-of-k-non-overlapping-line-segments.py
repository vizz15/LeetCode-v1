import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate C(n + k - 1, 2 * k) modulo 10^9 + 7
        return math.comb(n + k - 1, 2 * k) % MOD
