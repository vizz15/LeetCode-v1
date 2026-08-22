class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s1=str(n)
        l=list(s1)
        sum1=0
        p=1
        for i in l:
            sum1+=ord(i)-48
            p*=ord(i)-48
        if n%(sum1+p)==0:
            return True
        else:
            return False
        