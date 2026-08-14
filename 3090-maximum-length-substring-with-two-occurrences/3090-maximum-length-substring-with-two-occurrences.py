class Solution:
    def maximumLengthSubstring(self,s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                s2 = s[i:j]
            
                d = {}
                for k in range(len(s2)):  
                    d[s2[k]] = d.get(s2[k], 0) + 1

                if all(v <= 2 for v in d.values()):
                    max_len = max(max_len, len(s2))
                
        return max_len


        