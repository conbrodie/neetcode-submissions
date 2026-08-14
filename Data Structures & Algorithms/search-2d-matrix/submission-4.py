class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            rowLength = len(matrix[i]) - 1
            if target >= matrix[i][0] and target <= matrix[i][rowLength]:
                # binary search 
                l, r = 0, rowLength
                while l <= r:
                    mid = (l+r) // 2
                    if matrix[i][mid] == target:
                        return True
                    if matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
        
        return False

