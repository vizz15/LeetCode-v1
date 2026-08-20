class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1=[nums[0]]
        a2=[nums[1]]
        
        d1=0
        d2=0
        for i in range(2,len(nums)):
            if a1[d1]>a2[d2]:
                a1.append(nums[i])
                d1+=1
            else:
                a2.append(nums[i])
                d2+=1
        return a1+a2
