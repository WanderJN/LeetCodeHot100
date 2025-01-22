class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口，不断判断滑动窗口内是否满足，并记录长度

        occ = set()   # 哈希表

        max_len = 0
        n = len(s)
        right = 0
        for left in range(n):
            # 每次需要进入新元素（许多），直到碰到重复的就删除旧元素（第一个）
            while right < n and s[right] not in occ:
                occ.add(s[right])
                right += 1

            max_len = max(max_len, right - left)
            # 完成后，删除最前边的旧元素
            occ.remove(s[left])
        
        return max_len
