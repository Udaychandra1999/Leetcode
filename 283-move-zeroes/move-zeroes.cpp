class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        if(n==1|| n==0)
        {
            return;
        }
        queue<int> st;
        int count =0;
        for(int i =0;i<n;i++)
        {
            if(nums[i]!=0)
            {
                st.push(nums[i]);
            }
        }
        int i=0;
        while(!st.empty())
        {
            nums[i++] = st.front();
            st.pop();
        }
        while(i<n)
        {
            nums[i++]=0;
        }
    }
};