class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int res = nums[0]+nums[1]+nums[2];
        int n = nums.length;
        if(n==3)
        {
            return res;
        }
        int i,j,k;
        Arrays.sort(nums);
        for(i=0;i<n-2;i++)
        {
            j=i+1;
            k=n-1;
            while(j<k)
            {
                int s = nums[i]+nums[j]+nums[k];
                if(Math.abs(target-s)<Math.abs(res-target))
                {
                    res = s;
                }
                if(s<target)
                {
                    j++;
                }
                else
                {
                    k--;
                }
            }
        }
        return res;
    }
}