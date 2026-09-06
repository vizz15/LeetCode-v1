class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # dp[j] stores the number of subsequences matching t[0..j-1]
        # Base case: There is exactly 1 way to match an empty string t (dp[0] = 1)
        dp = [1] + [0] * n
        
        for i in range(1, m + 1):
            # Iterate backwards through t to use values from the previous iteration safely
            for j in range(n, 0, -1):
                if s[i - 1] == t[j - 1]:
                    dp[j] = dp[j] + dp[j - 1]
                    
        return dp[n]
