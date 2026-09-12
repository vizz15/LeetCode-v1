import bisect
import math

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        # Augment with original indices to retain their identity after sorting
        A = [(interval[0], interval[1], interval[2], i) for i, interval in enumerate(intervals)]
        # Sort intervals by their start times
        A.sort(key=lambda x: x[0])
        
        n = len(A)
        start_times = [x[0] for x in A]
        
        # Precompute the next non-overlapping interval index for each interval
        next_idx = [0] * n
        for i in range(n):
            next_idx[i] = bisect.bisect_right(start_times, A[i][1])
            
        # dp[i][rem] stores a tuple: (max_weight, sorted_tuple_of_indices)
        # initialized to a sentinel value representing invalid states
        dp = [[(-math.inf, ())] * 5 for _ in range(n + 1)]
        
        # Base case: choosing exactly 0 intervals yields 0 weight and an empty tuple
        for i in range(n + 1):
            dp[i][0] = (0, ())
            
        # Fill the DP table bottom-up
        for i in range(n - 1, -1, -1):
            l, r, w, orig_idx = A[i]
            nxt = next_idx[i]
            for rem in range(1, 5):
                # Option 1: Skip the current interval
                best_w, best_tuple = dp[i + 1][rem]
                
                # Option 2: Pick the current interval
                next_w, next_tuple = dp[nxt][rem - 1]
                if next_w != -math.inf:
                    pick_w = w + next_w
                    # Merge and sort the indices to keep the tuple sorted
                    pick_tuple = tuple(sorted(next_tuple + (orig_idx,)))
                    
                    # Maximize weight first, minimize indices lexicographically second
                    if pick_w > best_w:
                        best_w, best_tuple = pick_w, pick_tuple
                    elif pick_w == best_w:
                        if pick_tuple < best_tuple:
                            best_tuple = pick_tuple
                            
                dp[i][rem] = (best_w, best_tuple)
                
        # Find the overall best configuration across all allowed counts (0 to 4 intervals)
        overall_best_w = 0
        overall_best_idx = ()
        
        for k in range(1, 5):
            w, idx_tuple = dp[0][k]
            if w > overall_best_w:
                overall_best_w = w
                overall_best_idx = idx_tuple
            elif w == overall_best_w:
                if idx_tuple < overall_best_idx:
                    overall_best_idx = idx_tuple
                    
        return list(overall_best_idx)
