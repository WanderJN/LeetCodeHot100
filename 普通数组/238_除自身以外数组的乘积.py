class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 使用双指针，进行遍历
        # 左边指针正着乘累计，右边指针倒着乘累计，并以相乘形式更新结果数组

        ans = [1] * len(nums)
        left, right = 0, len(nums) - 1
        left_pre, right_pre = 1, 1

        # 双指针遍历，因为每个数其实都是前缀和后缀的乘积
        while right >= 0:
            # 正向遍历，乘以左边前缀
            ans[left] *= left_pre
            # 逆向遍历，乘以右边前缀
            ans[right] *= right_pre

            left_pre *= nums[left]
            right_pre *= nums[right]
            left += 1
            right -= 1
        
        return ans
        