class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        int score=0,curr_sum=0;
        int start =0;
        int i=0;
        map<int,int> mp;
        int n = nums.size();
        while (i<n){
            if(mp.find(nums[i])!=mp.end() && mp[nums[i]]>=start){
                while(start<=mp[nums[i]]){
                    curr_sum -= nums[start];
                    start++;
                }
            }
            mp[nums[i]] = i;
            curr_sum +=nums[i];
            score = score>curr_sum?score:curr_sum;
            i++;
        }
        return score;
    }
};