class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 贪心算法，每个点左上都比自己小，右下都比自己大，因此从左下角开始找
        i, j = len(matrix)-1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target:
                # 开始往上找
                i -= 1
            elif matrix[i][j] < target:
                # 开始往右找
                j += 1
            else:
                return True
        
        return False
