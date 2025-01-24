# 方法一，借助额外空间，空间复杂度O(m+n)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        result_row = set()
        result_col = set()
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if matrix[i][j] == 0:
                    result_row.add(i)
                    result_col.add(j)
        
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                if i in result_row or j in result_col:
                    matrix[i][j] = 0

# 方法二，不借助额外空间，空间复杂度O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 不借助额外空间实现矩阵置零
        # 具体实现是通过矩阵的第一行和第一列分别记录行和列需要置零的位置
        flag_row, flag_col = False, False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                flag_col = True
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                flag_row = True
        
        # 循环遍历矩阵，记录到第一行和第一列中
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # 再次遍历，根据第一行第一列进行更新
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 接下来需要将第一行和第一列再进行处理
        if flag_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if flag_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0