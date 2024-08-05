class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int res = Integer.MAX_VALUE;
        int n = nums.length;
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                for(int k=j+1;k<n;k++)
                {
                    int s = nums[i]+nums[j]+nums[k];
                    if(Math.abs(res-target)>Math.abs(s-target))
                    {
                        res = s;
                    }
                }
            }
        }
        return res;
    }
}