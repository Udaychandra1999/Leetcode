class Solution {
    public void solveSudoku(char[][] board) {
        boolean row[][] = new boolean[9][9];
        boolean col[][] = new boolean[9][9];
        boolean box[][] = new boolean[9][9];
        for (int i =0;i<9;i++) {
            for (int j=0;j<9;j++) {
                if (board[i][j] != '.') {
                    int n = board[i][j] - '0';
                    row[i][n-1] = true;
                    col[j][n-1] = true;
                    int b = (i/3)*3 + j/3;
                    box[b][n-1] = true;
                }
            }
        }
        backtrack(board,0,0,row,col,box);
    }
    public boolean backtrack(char[][] board,int i,int j,boolean[][] row,boolean[][] col,boolean[][] box)
    {
        if (i==9) return true;
        int ni,nj;
        if(j==8) {
            nj = 0;
            ni = i+1;
        }
        else {
            nj = j+1;
            ni = i;
        }
        if (board[i][j] != '.') {
            return backtrack(board,ni,nj,row,col,box);
        }
        else {
            int b = (i/3)*3 + j/3;
            for(int k=1;k<=9;k++)
            {
                if(!row[i][k-1] && !col[j][k-1] && !box[b][k-1]){
                    char c = (char)(k+'0');
                    board[i][j] = c;
                    row[i][k-1] = col[j][k-1] = box[b][k-1] = true;
                    if (backtrack(board,ni,nj,row,col,box)) {
                        return true;
                    }
                    board[i][j] = '.';
                    row[i][k-1] = col[j][k-1] = box[b][k-1] = false;
                }
                
            }
        }
        return false;
    }
}