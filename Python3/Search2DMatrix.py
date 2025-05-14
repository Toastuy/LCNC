class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Constants to make this easier to read
        ROWS, COLS = len(matrix), len(matrix[0])

        # First, perform binary search on the ROWS, figuring out which row our target is in
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                # This means we have found our row and go to the next step
                break
        
        # There is a chance we created an invalid condition though, so check first
        if not (top <= bot):
            return False

        # Now perform our second binary search on the row we found
        row = (top + bot) // 2
        left, right = 0, COLS - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        return False