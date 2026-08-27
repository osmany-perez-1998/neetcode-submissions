class Solution:

    def isValidSquare(self,board: List[List[str]], coord: tuple[int,int]):
        num_set =set()
        dot_count = 0
        sum = 0
        for i in range(3):
            for j in range(3):
                try:
                    box = int(board[coord[0]+ i][coord[1]+j])                    
                    num_set.add(box)
                    sum+=box
                except ValueError:
                    dot_count+=1
        
        return len(num_set) == (9-dot_count) and sum <=45        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):  
            num_set =set()
            dot_count = 0
            sum = 0         
            for j in range(len(board[0])):
                if i % 3 == 0 and j % 3 == 0 and not self.isValidSquare(board, (i,j)):
                    return False
                
                try:
                    box = int(board[i][j])                    
                    num_set.add(box)
                    sum+=box
                except ValueError:
                    dot_count+=1
            
            if not (len(num_set) == (9-dot_count) and sum <=45):
                return False
                               
                

        for j in range(len(board[0])): 
            num_set =set()
            dot_count = 0
            sum = 0   
            for i in range(len(board)):                
                try:
                    box = int(board[i][j])                    
                    num_set.add(box)
                    sum+=box
                except ValueError:
                    dot_count+=1
            
            if not (len(num_set) == (9-dot_count) and sum <=45):
                return False
        
        return True




        
