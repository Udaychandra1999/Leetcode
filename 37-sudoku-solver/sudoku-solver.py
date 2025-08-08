class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = board[i][j]
                    row[i].add(num)
                    col[j].add(num)
                    box[(i // 3) * 3 + j // 3].add(num)
                         
        def backtrack(board,i=0,j=0):
            if i == 9 :
                return True
            if board[i][j] != ".":
                if j<8:
                    return backtrack(board,i,j+1)
                else:
                    return backtrack(board,i+1,0)
            else:
                for k in range(1,10):
                    c= str(k)
                    if c not in row[i] and c not in col[j] and c not in box[(i // 3) * 3 + j // 3]:
                        board[i][j] = str(k)
                        row[i].add(c)
                        col[j].add(c)
                        box[(i // 3) * 3 + j // 3].add(c)
                        if j<8:
                            if backtrack(board,i,j+1):
                                return True
                        else:
                            if backtrack(board,i+1,0):
                                return True
                        board[i][j] = "."
                        row[i].remove(c)
                        col[j].remove(c)
                        box[(i // 3) * 3 + j // 3].remove(c)
            return False
        backtrack(board)
                     
            
        