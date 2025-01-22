class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maps = {}
        for i, num in enumerate(nums):
            if (target - num) in maps.keys():
                return [i, maps[target - num]]
            maps[num] = i