class Solution(object):
    ##动态规划
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = [0] * n
        ans[0] = 1
        for i in range(1, n):
            for j in range(i):
                ans[i] = max(ans[i], ans[j] * (i - j), (j + 1) * (i - j))

        return ans[n - 1]

    ##优化的动态规划 https://leetcode.cn/problems/integer-break/solutions/352875/zheng-shu-chai-fen-by-leetcode-solution/
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n-1

        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = max(2*(i-2), 2*dp[i-2], 3*(i-3), 3*dp[i-3])

        return dp[n]

    ## 数学
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
