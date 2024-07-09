class Solution {
    public void nextPermutation(int ar[],int flag[],int n,List<Integer> stk,int flc,List<List<Integer>> res)
    {
        if(flc ==n)
        {
            //add to res;
            res.add(new ArrayList<>(stk));
            return;
        }
        for(int i =0;i<n;i++)
        {
            if(flag[i] ==0)
            {
                stk.add(ar[i]);
                flag[i] =1;
                nextPermutation(ar,flag,n,stk,flc+1,res);
                flag[i] = 0;
                stk.remove(stk.size()-1);
            }
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        int n = nums.length;
        List<Integer> stk = new ArrayList<>();
        int flag[] = new int[n];
        Arrays.fill(flag,0);
        List<List<Integer>> res = new ArrayList<>();
        nextPermutation(nums,flag,n,stk,0,res);
        return res;
    }
}