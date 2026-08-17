class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        
        # 1. Total cumulative prefix sum array
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        # 2. DP matrices to keep track of running maxes
        # dp[i][j]: max score for subarray stoneValue[i...j]
        # max_l[i][j]: max of (dp[i][k] + sum(i...k)) for k in range i...j
        # max_r[i][j]: max of (dp[k][j] + sum(k...j)) for k in range i...j
        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]
        
        # Base case initializations for single stones
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        # 3. Process subarrays from shortest length to longest
        for length in range(2, n + 1):
            k = 0  # Sliding split pointer where sum(left) >= sum(right)
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Move 'k' forward while the left side sum is strictly less than the right side sum
                while pref[k + 1] - pref[i] < pref[j + 1] - pref[k + 1]:
                    k += 1
                    
                # Case A: If left sum equals right sum exactly at split 'k'
                if pref[k + 1] - pref[i] == pref[j + 1] - pref[k + 1]:
                    dp[i][j] = max(max_l[i][k], max_r[k + 1][j])
                else:
                    # Case B: Pick the best score from either side of the boundary split
                    score_left = max_l[i][k - 1] if k > i else 0
                    score_right = max_r[k + 1][j] if k < j else 0
                    dp[i][j] = max(score_left, score_right)
                    
                # Update the running max helper tables for the next length level
                total_sum = pref[j + 1] - pref[i]
                max_l[i][j] = max(max_l[i][j - 1], dp[i][j] + total_sum)
                max_r[i][j] = max(max_r[i + 1][j], dp[i][j] + total_sum)
                
        return dp[0][n - 1]
