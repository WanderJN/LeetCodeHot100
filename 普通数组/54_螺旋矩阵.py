class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m, n = len(matrix), len(matrix[0])

        # 记录当前的圈数
        roll = 0
        # 死循环，直到输出结果长度和总长度一致
        while True:
            # 从左向右横向遍历，左闭右闭
            for j in range(roll, n-roll):
                result.append(matrix[roll][j])
            if len(result) == m*n: break

            # 从上向下纵向遍历，上开下开
            for i in range(roll+1, m-roll-1):
                result.append(matrix[i][n-roll-1])
            if len(result) == m*n: break

            # 从右向左横向遍历，左闭右闭
            for j in range(n-roll-1, roll-1, -1):
                result.append(matrix[m-roll-1][j])
                print(matrix[m-roll-1][j])
            if len(result) == m*n: break
            
            # 从下向上纵向遍历，上开下开
            for i in range(m-roll-1-1, roll, -1):
                result.append(matrix[i][roll])
            if len(result) == m*n: break

            # 每完成一圈，就加一
            roll += 1
        
        return result
