class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n=len(s)
        for i in range(n):
            if len(s)==2 and s[::-1]==s:
                return True
            if i<n-1:
                sub=abs(ord(s[i])-ord(s[i+1]))
                if sub==1 or sub==2 or sub==0:
                    continue
                else:
                    return False
                    break
            return True


        