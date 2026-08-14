class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        top, bottom = 0, rows - 1
        row = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][columns - 1]:
                top = mid + 1
            else:
                row = mid
                break

        if row == -1:
            return False

        l, r = 0, columns - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        
        return False
