class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        count = {}
        left = 0
        ans = 0
        
        for right, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1
            
            while count[num] > k:
                count[nums[left]] -= 1
                left += 1
                
            ans = max(ans, right - left + 1)
            
        return ans
