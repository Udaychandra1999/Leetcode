class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n,0);
        int l =0,r=n-1;
        for(int i=n-1;i>-1;i--)
        {
            int val;
            if( abs(nums[l])>abs(nums[r]) )
            {
                val = nums[l];
                l++;
            }
            else
            {
                val = nums[r];
                r--;
            }
            res[i]=val*val;
        }
        return res;
    }
};