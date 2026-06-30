class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        x2=x.lower()
        x3=x2[::-1]
        if x3==x:
            return True 
        else:
            return False    