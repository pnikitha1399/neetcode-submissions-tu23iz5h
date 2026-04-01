class Solution:
    def climbStairs(self, n: int) -> int:
        #recursion
        # def dfs(i):
        #     if i>=n:
        #         return i==n
        #     return dfs(i+1)+dfs(i+2)
        # return dfs(0)


        #top down
        # cache = [-1]*n
        # def dfs(i):
        #     if i>=n:
        #         return i==n
        #     if cache[i]!=-1:
        #         return cache[i]
        #     cache[i]=dfs(i+1)+dfs(i+2)
        #     return cache[i]
        # return dfs(0)

        #bottom up
        # if n<=2:
        #     return n
        # dp = [0]*(n+1)
        # dp[1], dp[2] = 1, 2
        # for i in range(3, n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]

        #space optimized
        one, two = 1, 1
        for i in range(n-1):
            t = one
            one = one + two
            two = t
        return one