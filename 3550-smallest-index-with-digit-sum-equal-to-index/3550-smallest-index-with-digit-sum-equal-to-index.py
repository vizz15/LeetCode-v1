class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        res=[]
        i=0
        ans=False

        for j in nums:
            digit_sum=sum(int(digit) for digit in str(abs(j)))
            if digit_sum==i:
                res.append(i)
                ans=True
            i+=1
        if ans==True:
            return min(res)
        else:
            return -1