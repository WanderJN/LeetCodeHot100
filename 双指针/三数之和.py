class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 先对列表进行排序
        nums = sorted(nums)
        len_ = len(nums)

        for i in range(len_):
            # 如果第一个数就超过0，直接跳过
            if nums[i] > 0:
                return result
            # 对第一个数去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 双指针法取第2和第3个数字
            j = i + 1
            k = len_ - 1
            while j < k:
                if nums[i] + nums[j] + nums[k]  < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    # 已经得到结果之后，再去重
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    # 找到结果之后收缩区间
                    k -= 1
                    j += 1
        
        return result

        