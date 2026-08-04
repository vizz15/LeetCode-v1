class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        c=0
        s=[]
        for i in range(b-a):
            num=a+c
            if num in nums:
                c+=1
                continue
            elif num not in nums and num<b:
                s.append(num)
            c+=1
        return sorted(s)



        