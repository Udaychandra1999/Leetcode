class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int start=0;
        int curr_sum=0,max_sum=0;
        unordered_map<int,int> mp;
        for(int end= 0;end<nums.size();end++){
            if(mp.find(nums[end])!=mp.end() && mp[nums[end]]>=start){
                while(start<=mp[nums[end]]){
                    curr_sum -= nums[start];
                    start++;
                }
            }
            mp[nums[end]] = end;
            curr_sum += nums[end];
            max_sum = max(curr_sum,max_sum);
        }
        return max_sum;
    }
};