class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count=0
        for i in range(0,len(nums)):
            if target==nums[i]:
                return i
            elif target < nums[i]:
                return i
            else:
                count+=1
        return count


                 
       