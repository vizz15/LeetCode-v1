class Solution:

    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)

        # suffix_sums[i] stores the total number of stones from index i to the end
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            # Base case: If we can take all the remaining piles, take them all!
            if i + 2 * m >= n:
                return suffix_sums[i]

            # Look up cache to avoid redundant work
            if (i, m) in memo:
                return memo[(i, m)]

            max_stones = 0
            # Try taking X piles where 1 <= X <= 2M
            for x in range(1, 2 * m + 1):
                # Current player's score = Total remaining - Opponent's optimal score next turn
                opponent_score = dp(i + x, max(m, x))
                current_score = suffix_sums[i] - opponent_score
                max_stones = max(max_stones, current_score)

            memo[(i, m)] = max_stones
            return max_stones

        # Alice starts at index 0 with M = 1
        return dp(0, 1)
