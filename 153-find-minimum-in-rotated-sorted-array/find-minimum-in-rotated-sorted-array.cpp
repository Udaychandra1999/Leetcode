class Solution {
public:
    int min(int a,int b)
    {
        return a>b?b:a;
    }
    int findMin(vector<int>& nums) {
        int res = nums[0];
        int low,high,mid;
        low = 0;
        high = nums.size()-1;
        while(low<=high){
            mid = (low+high)/2;
            // left sorted array
            if(nums[low]<=nums[mid]){
                res = min(res,nums[low]);
                low = mid+1;
            }
            else if(nums[mid]<=nums[high])
            {
                res = min(res,nums[mid]);
                high = mid-1;
            }
        }
        return res;
    }
};