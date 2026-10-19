class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            first = matrix[mid][0]
            last = matrix[mid][-1] 

            if target < first:
                right = mid - 1
            elif target > last:
                left = mid + 1


            elif first <= target and target <= last:
                row = matrix[mid]
                col_left = 0
                col_right = len(row) - 1

                while col_left <= col_right:
                    col_mid = (col_left + col_right) // 2
                    if row[col_mid] < target:
                        col_left = col_mid + 1
                    elif row[col_mid] > target:
                        col_right = col_mid - 1
                    else:
                        return True

                return False

        return False
                    
                    
                
                

                
                


        