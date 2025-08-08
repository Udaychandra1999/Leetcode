class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    #horizontal check
                    for k in range(9):
                        if k!=j and board[i][j] == board[i][k]:
                            return False
                    #vertical check
                    for k in range(9):
                        if k!=i and board[i][j] == board[k][j]:
                            return False
                    #box check
                    r,c = (i//3) * 3, (j//3) * 3
                    for h in range(r,r+3):
                        for v in range(c,c+3):
                            if h != i or v != j:
                                if board[i][j] == board[h][v]:
                                    return False
        return True
                            
        