class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        ways=[1,2]

        for i in range(2,n):
            nx=ways[i-1]+ways[i-2]
            ways.append(nx)
        return ways[-1]

        