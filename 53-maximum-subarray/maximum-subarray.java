class Solution {
    public static int max(int a,int b)
        {
            if(a>b)
                return a;
            return b;
            
        }
    public int maxSubArray(int[] nums) {
        int sum =0;
        int smax = Integer.MIN_VALUE;
        
        for(int i: nums)
        {
            sum+=i;
            smax = max(sum,smax);
            sum = sum>0?sum:0;
        }
        return smax;
    }
}