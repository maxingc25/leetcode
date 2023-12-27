class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        count = 0
        ans = float('-inf')
        for i in range(len(nums)):
            count += nums[i]
            ans = max(ans, count)
            if count < 0:
                count = 0

        return ans