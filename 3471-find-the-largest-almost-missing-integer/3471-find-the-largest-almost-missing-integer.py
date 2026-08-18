class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # Fix 1: Handle k == n case first
        if k == n:
            return max(nums)
            
        # Fix 2: Handle k == 1 case properly by looking for elements with count == 1
        if k == 1:
            candidates = [x for x in nums if nums.count(x) == 1]
            return max(candidates) if candidates else -1
            
        # Fix 3: For 1 < k < n, only check the absolute edges for a count of EXACTLY 1
        count1 = nums.count(nums[0])
        count2 = nums.count(nums[n-1])
        
        candidates = []
        if count1 == 1:
            candidates.append(nums[0])
        if count2 == 1:
            candidates.append(nums[n-1])
            
        return max(candidates) if candidates else -1
