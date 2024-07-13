class Solution {
    public int nCr(int n,int r)
    {
        int prod =1;
        int re = (n-r)<r?(n-r):r;
        for(int i=0;i<re;i++)
        {
            prod = prod*(n-i);
            prod = prod/(i+1);
        }
        return prod;
    }
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<numRows;i++)
        {
            List<Integer> l = new ArrayList<>();
            if(i==0)
            {
                l.add(1);
                res.add(l);
            }
            else
            {
            for(int j=0;j<=i;j++)
            {
                l.add(nCr(i,j));
            }
            res.add(l);
            }
            
        }
        return res;
    }
}