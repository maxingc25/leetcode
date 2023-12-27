class Solution:
    ##方法一 记忆化搜索/动归
    @cache
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1

        return self.fib(n-1) + self.fib(n-2)

    ##https: // leetcode.cn / problems / climbing - stairs / solution / pa - lou - ti - by - leetcode - solution /
    ##方法二 矩阵快速幂

    ##方法三 通项公式

