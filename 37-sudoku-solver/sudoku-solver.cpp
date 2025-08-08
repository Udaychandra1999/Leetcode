class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
       vector<vector<bool>> row(9,vector<bool>(9,false));
       vector<vector<bool>> col(9,vector<bool>(9,false));
       vector<vector<bool>> box(9,vector<bool>(9,false));
       for(int i=0;i<9;i++) {
        for(int j=0;j<9;j++) {
            if (board[i][j]!='.') {
                int num = board[i][j] - '1';
                row[i][num] = true;
                col[j][num] = true;
                box[(i/3)*3+(j/3)][num] = true;
            }
        }
       }
       backtrack(board,0,0,row,col,box);
    }
    bool backtrack(vector<vector<char>>& board,int i,int j,vector<vector<bool>>& row,vector<vector<bool>>& col,vector<vector<bool>>& box)
    {
        if (i==9) {
            return true;
        }
        int ni,nj;
        if (j==8) {
            ni = i+1;
            nj = 0;
        } else {
            ni = i;
            nj = j+1;
        }
        
        if (board[i][j] != '.') {
            return backtrack(board,ni,nj,row,col,box);
        }
        for (int k=1;k<=9;k++) {
            int b = (i/3) *3 + (j/3);
            if (!row[i][k-1] && !col[j][k-1] && !box[b][k-1]) {
                board[i][j] = (char)(k+'0');
                row[i][k-1] = col[j][k-1] = box[b][k-1] = true;
                if (backtrack(board,ni,nj,row,col,box)) return true;
                row[i][k-1] = col[j][k-1] = box[b][k-1] = false;
                board[i][j] = '.';
            }
        }
        return false;
    }
};