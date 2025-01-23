class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 优先级队列
        n = len(nums)
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)       # 将q转化为优先级队列，小根堆

        ans = [-q[0][0]]   # 第一个结果就是最大值
        for i in range(k, n):
            # 每次加入一个新元素
            heapq.heappush(q, (-nums[i], i))
            # 但删除元素时，小的元素可以忽略，先不删除
            # 需要判断当前最大的元素是不是在i-k之前的，如果是就需要全部剔除掉，而其余小的元素不需要剔除
            while q[0][1] <= i - k:
                heapq.heappop(q)

            # 获取新的最大值
            ans.append(-q[0][0])
        return ans
