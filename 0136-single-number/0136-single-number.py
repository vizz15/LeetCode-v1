class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        dict={}

        for i in range(n):
            if(nums[i] in dict):
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1

        # Finds the first key with a value of 1
        for key,value in dict.items():
            if value==1:
                return key
        


        
        