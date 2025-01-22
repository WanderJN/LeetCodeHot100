class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = {}
        # 以26个字母为键，构建哈希表
        for word in strs:
            # 获取每个单词的键key
            key = [0] * 26
            for i in word:
                key[ord(i) - ord('a')] += 1
        
            # 判断当前键是否存在于哈希表中，注意必须是tuple元组的格式
            if tuple(key) not in maps.keys():
                maps[tuple(key)] = [word]
            else:
                maps[tuple(key)].append(word)
        
        # 最后再返回maps的values，并转化为list格式
        return list(maps.values())
                