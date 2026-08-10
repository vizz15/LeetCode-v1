class Solution:
    def winnerSquareGame(self, n: int) -> bool: # internal name can vary, e.g., winnerSquareGame
        # dp[i] will store True if the player whose turn it is can win with 'i' stones remaining
        dp = [False] * (n + 1)
        
        # Base case: dp[0] is False because a player with 0 stones cannot make a move and loses.
        
        for i in range(1, n + 1):
            # Try removing every possible perfect square k*k
            k = 1
            while k * k <= i:
                # If removing k*k stones leaves the opponent in a losing state (dp[i - k*k] == False),
                # then the current player wins!
                if not dp[i - k * k]:
                    dp[i] = True
                    break # No need to check other squares for this 'i'
                k += 1
                
        return dp[n]

        

        