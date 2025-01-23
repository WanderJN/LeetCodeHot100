class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 先统计个数，然后用小根堆逐个进入然后达到k时，进入一个弹出一个，确保堆里只有k个元素
        map_ = {}
        for i in nums:
            if map_.__contains__(i):
                map_[i] += 1
            else:
                map_[i] = 1
        
        # 创建小根堆，并逐步通过循环加入元素
        q = []
        for (i, j) in map_.items():
            heapq.heappush(q, (j, i))
            if len(q) > k:
                heapq.heappop(q)
            
        # 现在堆只有最大的k个数
        result = []
        for j, i in q:
            result.append(i)
        
        return result