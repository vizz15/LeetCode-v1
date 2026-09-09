class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        start = 1000
        
        # Add the contribution of each comma threshold layer
        while start <= n:
            total_commas += (n - start + 1)
            start *= 1000  # Advance to the next comma layer (million, billion, etc.)
            
        return total_commas
