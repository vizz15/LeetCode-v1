class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        # If target is negative, it's impossible.
        if target < 0:
            return -1
        # If target is zero, we must remove all elements.
        if target == 0:
            return len(nums)
            
        max_len = -1
        current_sum = 0
        left = 0
        
        # Sliding window to find the longest subarray summing to target
        for right in range(len(nums)):
            current_sum += nums[right]
            
            # Shrink window if the sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            # Check if we hit the exact target sum
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        # If no valid subarray was found, return -1
        return len(nums) - max_len if max_len != -1 else -1
