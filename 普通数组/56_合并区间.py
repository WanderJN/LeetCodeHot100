class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先对列表进行排序
        intervals.sort(key=lambda x:x[0])

        result = []
        for interval in intervals:
            # 如果当前合并列表为空，或者无法合并，直接加入子数组
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                # 否则，按合并的方式去修改数组
                result[-1][1] = max(result[-1][1], interval[1])
        return result
        