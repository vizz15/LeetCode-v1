class Solution:
    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        # dp[i] stores the maximum relative score leading player can get from index i to the end
        dp = [0] * (n + 1)
        
        # Look at the game backwards from the last stone to the first stone
        for i in range(n - 1, -1, -1):
            # Option 1: Take 1 stone
            take1 = stoneValue[i] - dp[i + 1]
            
            # Option 2: Take 2 stones (if available)
            take2 = stoneValue[i] + stoneValue[i + 1] - dp[i + 2] if i + 1 < n else float('-inf')
            
            # Option 3: Take 3 stones (if available)
            take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3] if i + 2 < n else float('-inf')
            
            # Pick the best choice out of the 3 options
            dp[i] = max(take1, take2, take3)
            
        # dp[0] tells us Alice's net advantage over Bob at the start of the game
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            # If the advantage is negative, it means Bob wins
            return "Bob"
        else:
            return "Tie"
