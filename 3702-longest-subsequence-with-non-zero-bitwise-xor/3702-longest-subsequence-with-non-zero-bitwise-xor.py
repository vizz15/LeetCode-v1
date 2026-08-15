class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total=0
        has_nonzero=False
        for num in nums:
            total^=num
            if total>0:
                has_nonzero= True
        if not has_nonzero:
            return 0
        elif total!=0:
            return len(nums)
        elif total==0:
            return len(nums)-1
        else:
            return 0 