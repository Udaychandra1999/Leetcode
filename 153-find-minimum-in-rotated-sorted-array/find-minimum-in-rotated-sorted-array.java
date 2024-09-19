class Solution {
    public static int min(int a, int b)
    {
        return a>b?b:a;
    }
    public int findMin(int[] nums) {
        int res = Integer.MAX_VALUE;
        int low =0,high = nums.length-1;
        while(low<=high)
        {
            //mid value
            int mid = (low+high)/2;
            //check left sorted 
            if(nums[low]<=nums[mid])
            {
                res = min(res,nums[low]);
                low = mid+1;
            }
            else
            {
                res = min(res,nums[mid]);
                high = mid -1;
            }
        }
        return res;
    }
}