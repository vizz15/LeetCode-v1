class Solution:
    def maxDepth(self, s: str) -> int:
        ans =0
        st=[]
        for c in s:
            if c=="(":
                st.append(c)
            elif c==")":
                st.pop()
            ans=max(ans,len(st))
        return ans
