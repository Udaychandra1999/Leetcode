class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> temp;
        for(auto i:nums)
        {
            if(temp.empty()|| temp.back()!=i)
            {
                temp.push_back(i);

            }
        }
        swap(nums,temp);
        return nums.size();
    }
};