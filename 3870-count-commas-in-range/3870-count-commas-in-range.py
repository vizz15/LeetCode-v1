class Solution:
    def countCommas(self, n: int) -> int:
        if 1000<=n<=100000:
            return n-999
        else:
            return 0
        