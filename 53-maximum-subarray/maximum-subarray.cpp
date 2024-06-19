class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int su=0;
        int smax = INT_MIN;
        for(int i: nums)
        {
            su+=i;
            smax = max(su,smax);
            if (su<0)   su =0;
        }
        return smax;
    }
};