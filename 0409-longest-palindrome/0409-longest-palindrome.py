class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        n=len(s)
        for i in range(n):
            d[s[i]]=d.get(s[i],0)+1
        count=0
        odd=0
        for key,value in d.items():
            if d[key]%2 == 0:
                count+=d.get(key)
            elif d[key]%2 !=0:
                odd+=1
                count+=d.get(key)
            #odd
        oddd=0
        if odd!=0:
            oddd=odd-1
        return(count-oddd)
