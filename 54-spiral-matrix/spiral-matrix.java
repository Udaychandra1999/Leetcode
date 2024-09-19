class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        int m,n;
        m = matrix.length;
        n = matrix[0].length;
        int top=0,bottom = m-1,left=0,right = n-1;
        while(left<right && top<bottom)
        {
        //right , top is constant
            for(int i =left;i<=right;i++)
            {
                res.add(matrix[top][i]);
            }
            top++;
            //down , right is constant
            for(int i=top;i<=bottom;i++)
            {
                res.add(matrix[i][right]);
            }
            right--;
            //left ,bottom is constant
            for(int i = right;i>=left;i--)
            {
                res.add(matrix[bottom][i]);
            }
            bottom--;
            //up , left is constant
            for(int i=bottom;i>=top;i--)
            {
                res.add(matrix[i][left]);
            }
            left ++;
        }
        if(top==bottom && left == right) //only one element
        {
            res.add(matrix[top][right]);
        }
        else if(top == bottom) // one row
        {
            for(int i=left;i<=right;i++)
            {
                res.add(matrix[top][i]);
            }
        }
        else if(left==right) //one col
        {
            for(int i=top;i<=bottom;i++)
            {
                res.add(matrix[i][left]);
            }
        } 
        return res;
    }
}