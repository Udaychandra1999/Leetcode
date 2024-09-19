class Solution {
    public int searchInsert(int[] nums, int target) {
        int high=nums.length-1,low=0;
        while(low<=high)
        {
            int mid = (low+high)/2;
            if(nums[mid] == target)
            {
                return mid;
            }
            else if(nums[mid]>target)
            {
                high = mid -1;
            }
            else
            {
                low = mid+1;
            }
        }
        return high+1;
    }
}