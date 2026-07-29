class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        left = 0
        right = len(matrix[0]) - 1

        while row < len(matrix):
            if matrix[row][right] < target:
                row += 1
            else:
                break
        else:
            return False


        while left <= right:

            mid = left + int((right - left) / 2)

            if matrix[row][mid] == target:
                return True
            
            elif matrix[row][mid] < target:
                left = mid + 1

            else:
                right = mid - 1


        return False

            


            

        
