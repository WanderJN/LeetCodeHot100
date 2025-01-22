class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            now_area = (right - left) * min(height[right], height[left])
            max_area = max(now_area, max_area)

            # 哪边指针的高度小，则需要移动哪边
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return max_area
