class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        result = []
        if s_len < p_len:
            return result

        # 滑动窗口
        left, right = 0, 0

        p_map = [0] * 26
        s_map = [0] * 26
        # 先初始化滑动窗口填入数组中
        while right < p_len:
            p_map[ord(p[right]) - ord('a')] += 1
            s_map[ord(s[right]) - ord('a')] += 1
            right += 1

        # 先判断一次当前是否满足要求
        if s_map == p_map:
            result.append(left)
        
        while right < s_len:
            # 每次进入一个元素，删除一个元素，滑动窗口长度保持不变
            s_map[ord(s[right]) - ord('a')] += 1
            right += 1
            s_map[ord(s[left]) - ord('a')] -= 1
            left += 1
            
            # 直接判断当前是否满足要求
            if s_map == p_map:
                result.append(left)

        return result
        