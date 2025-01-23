class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        # 前缀和
        pre_sum = 0
        min_pre_sum = 0
        for i in nums:
            pre_sum += i

            # 当前前缀和减去最小的前缀和，即可得到最大的中间数组
            ans = max(ans, pre_sum - min_pre_sum)
            # 循环去维护最小的前缀和
            min_pre_sum = min(pre_sum, min_pre_sum)
        
        return ans
