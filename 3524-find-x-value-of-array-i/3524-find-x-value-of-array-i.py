class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        # result[x] will store the total number of subarrays whose product % k == x
        result = [0] * k
        
        # dp[r] tracks the count of subarrays ending at the current position 
        # that have a running product modulo k equal to r
        dp = [0] * k
        
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            
            # Case 1: Start a brand new single-element subarray at the current number
            new_dp[num_mod] += 1
            
            # Case 2: Extend all valid subarrays that ended at the previous number
            for r in range(k):
                if dp[r] > 0:
                    new_rem = (r * num_mod) % k
                    new_dp[new_rem] += dp[r]
            
            # Accumulate the counts of all subarrays ending at this position into the grand total
            for r in range(k):
                result[r] += new_dp[r]
                
            # Move to the next element
            dp = new_dp
            
        return result
