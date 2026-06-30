class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        x2=x.lower()
        x3=x2[::-1]
        if x==x3:
            return True 
        else:
            return False       