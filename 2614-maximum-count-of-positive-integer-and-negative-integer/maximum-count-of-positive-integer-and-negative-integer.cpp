class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int low,high,mid,pos,neg;
        low =0;high = nums.size()-1;
        pos=0;neg=0;
        // postive phase
        while (low<=high){
            mid = (low+high)/2;
            if(nums[mid]>0){
                pos += high - mid +1;
                high = mid -1;
            }
            else {
                low = mid+1;
            }
        }
        // negative phase
        low=0;high = nums.size()-1;
        while(low<=high){
            mid = (low+high)/2;
            if(nums[mid]<0){
                neg += mid-low+1;
                low = mid+1;
            }
            else {
                high = mid-1;
            }
        }
        return pos>neg?pos:neg;
    }
};