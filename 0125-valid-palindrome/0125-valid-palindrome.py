class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=list(s)
        lis1=[]
        for i in st:
            if i.isalnum():
                lis1.append(i.lower())
        str1="".join(lis1)
        if str1=="":
            return True
        else:
            return str1.lower()==str1[::-1]
                    
            
        