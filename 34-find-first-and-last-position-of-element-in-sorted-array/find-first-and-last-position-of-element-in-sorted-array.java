class Solution {
    public static int getLowerBound(int[] nums,int target)
    {
        int ans =nums.length;
        int low=0,high=nums.length-1;
        while(low<=high)
        {
            int mid =(low+high)/2;
            if(nums[mid]>=target)
            {
                ans = mid;
                high = mid-1;
            }
            else
            {
                low = mid+1;
            }
        }
        return ans;
    }
    public static int getUpperBound(int[] nums,int target)
    {
        int ans = nums.length;
        int low = 0,high = nums.length-1;
        while(low<=high)
        {
            int mid = (low+high)/2;
            if(nums[mid]>target)
            {
                ans = mid;
                high = mid-1;
            }
            else
            {
                low = mid+1;
            }
        }
        return ans;
    }
    public int[] searchRange(int[] nums, int target) {
        int f,l;
        f= getLowerBound(nums,target);
        if (f==nums.length || nums[f]!=target) return new int[] {-1,-1};
        return new int[] {f,getUpperBound(nums,target)-1};
        
    }
}