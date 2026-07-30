class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        e=list(s1.split())
        f=list(s2.split())
        g=[]
        for items in e:
            if e.count(items)>=2:
                continue
            if items not in f:
                g.append(items)
        for items1 in f:    
            if f.count(items1)>=2:
                continue
            if items1 not in e:
                g.append(items1)
        return g