from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        num_set = set()
        nums = []
        
        #Squares
        for i in range(3):
            for j in range(3):
                #Corner
                k = i*3
                l = j*3

                for m in range(3):
                    for n in range(3):
                        if board[k+m][l+n] != ".":
                            num_set.add(board[k+m][l+n])
                            nums.append(board[k+m][l+n])
                
                if len(num_set) != len(nums):
                    return False
                
                num_set.clear()
                nums = []
        
        #Horizontal
        for j in range(9):
            for i in range (9):
                if board[i][j] != ".":
                    num_set.add(board[i][j])
                    nums.append(board[i][j])
            if len(num_set) != len(nums):
                return False

            num_set.clear()
            nums = []

        #Vertical
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num_set.add(board[i][j])
                    nums.append(board[i][j])
            if len(num_set) != len(nums):
                return False
            num_set.clear()
            nums = []

        return True



        