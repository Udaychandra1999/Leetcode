class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                else:
                    t = board[i][j]
                    if t in rowset[i] or t in colset[j] or t in boxset[i//3,j//3]:
                        return False
                    rowset[i].add(t)
                    colset[j].add(t)
                    boxset[i//3,j//3].add(t)
        return True
                    
                            
        