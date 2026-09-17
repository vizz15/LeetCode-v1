class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # min_len[i] stores the minimum length of a valid sub-array ending at or before index i
        min_len = [float('inf')] * n
        
        left = 0
        current_sum = 0
        min_so_far = float('inf')
        ans = float('inf')
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            # If a valid sub-array is found
            if current_sum == target:
                curr_len = right - left + 1
                
                # If there's a valid non-overlapping sub-array to the left of the current one
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                
                # Update the running minimum length
                min_so_far = min(min_so_far, curr_len)
            
            # Store the historical minimum length up to the current index
            min_len[right] = min_so_far
            
        return ans if ans != float('inf') else -1
