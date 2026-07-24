class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        pattern1=[s.find(char) for char in s]
        pattern2=[t.find(char) for char in t]

        return pattern1==pattern2 