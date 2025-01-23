class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 这题里边会存在复数，因此滑动窗口法无效（无法通过判断当前sum小于k或大于k去调整滑动窗口大小）
        # 需要用到前缀和的方法
        sum_num = 0
        count = 0

        map_ = {}
        map_[0] = 1    # 必须将0添加进去，否则sum_num - k为0的前缀和会被忽略（初始时）

        for i in nums:
            sum_num += i    # 获取前缀和
            # 如果现在的前缀和 减去 以前的前缀和为 k， 则证明中间存在连续的数字和为k
            if map_.__contains__(sum_num - k):
                count += map_[sum_num - k]  # 这里会存在重复的，但是位置不一样的结果

            # 如果前缀和里包括，就计数+1，否则初始化为1
            if map_.__contains__(sum_num):
                map_[sum_num] += 1
            else:
                map_[sum_num] = 1
        
        return count
