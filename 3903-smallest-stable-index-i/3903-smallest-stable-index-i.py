class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        nums1=[]
        n=len(nums)
        for i in range(0,len(nums)):
            nums1.append(nums[0])
            ins=max(nums1)-min(nums)
            del nums[0]
            if ins <= k:
                return i
            elif not ins<= k and i==n-1:
                return -1
                