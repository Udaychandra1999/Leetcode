class Solution {
    public void swap(int[][] matrix,int i,int j)
    {
        int temp = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = temp;
    }
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        //transpose matrix
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(i<j) swap(matrix,i,j);
            }
        }
        //reverse matrix
        for(int i=0;i<n;i++)
        {
            int l =0,r=n-1;
            while(l<r)
            {
                int temp = matrix[i][l];
                matrix[i][l] = matrix[i][r];
                matrix[i][r] = temp;
                l++;
                r--;
            }
        }
    }
}