class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 如果没有0，快慢指针一直指向同一个元素，如果有0，快指针先走一步，然后和慢指针（当前刚好为0）进行交换
        # 左指针始终在维护一个非0的数组，右指针一直在往右走查看有没有非0的数值，有的话就需要交换
        left = right = 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1