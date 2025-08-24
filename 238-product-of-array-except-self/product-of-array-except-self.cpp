class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        int x = 1;
        for(int i=0;i<nums.size();i++) {
            res.push_back(x);
            x = x*nums[i];
        }
        x = 1;
        for(int i=nums.size() -1;i>=0;i--) {
            res[i] *= x;
            x = x*nums[i];
        }
        return res;
    }
};