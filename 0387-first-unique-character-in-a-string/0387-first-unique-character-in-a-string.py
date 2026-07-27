class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1={}
        count=0
        for i in s:
            dict1[i]=dict1.get(i,0)+1
        for v in range(len(s)):
            if dict1[s[v]]<2:
                return count
                break
            count+=1
        return -1
        