# 解法1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 先使用set去重
        length_max = 0
        nums = set(nums)

        for num in nums:
            # 如果当前的数字上一个数字不在集合中，那么从当前数字开始计数
            if num - 1 not in nums:
                current_num = num
                length_now = 1
                
                # 从当前数字往后加1，不断查找有没有该数字在集合中
                while (current_num + 1 in nums):
                    current_num += 1
                    length_now += 1
                
                length_max = max(length_max, length_now)
        
        return length_max

# 解法二：
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # 先从小到大排序
        nums = set(nums)
        nums = sorted(nums)

        # 循环遍历查找最长子序列
        i = 1
        result = 1
        max_result = 1
        # 外循环遍历全部数组
        while i < len(nums):
            # 内循环去看当前元素是否一直比前一个元素大1，并不断更新i
            while i < len(nums) and nums[i] - nums[i-1] == 1:
                result += 1
                i += 1
            
            max_result = result if result > max_result else max_result
            result = 1
            i += 1
        
        return max_result