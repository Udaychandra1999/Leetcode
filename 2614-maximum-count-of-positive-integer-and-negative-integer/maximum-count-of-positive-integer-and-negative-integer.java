class Solution {
    public int maximumCount(int[] nums) {
        int low,high,mid,pos,neg;
        low =0;high=nums.length-1;pos=neg=0;
        //positive side
        while(low<=high){
            mid = (low+high)/2;
            if(nums[mid]>0){
                pos += high -mid +1;
                high = mid -1;
            }
            else {
                low = mid +1;
            }
        }
        //negative side
        low =0;high = nums.length-1;
        while(low<=high){
            mid = (low+high)/2;
            if(nums[mid]<0){
                neg += mid -low+1;
                low = mid+1;
            }
            else {
                high = mid -1;
            }
        }
        return pos>neg?pos:neg;
    }

}