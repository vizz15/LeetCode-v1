class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        m=0
        d={}
        lexi=""
        for i in range(0,len(s)+1):
            for j in range(i,len(s)+1):
                lexi=s[i:j]
                for char in lexi:
                    if char=="1":
                        m+=1
                    else:
                        continue
                if m==k:
                    if len(lexi)>=m:
                        d[lexi]=d.get(lexi,len(lexi))
                m=0
        if len(d)>0:
            return min(d.keys(), key=lambda x: (len(x), x))
        else:
            return ""
                