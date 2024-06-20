class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int counter=0;
        int i =1;
        while(i<nums.size())
        {
            if(nums[counter]==nums[i])
            {
                i++;
            }
            else
            {
                nums[counter+1] = nums[i];
                counter++;
            }
        }
        return counter+1;
    }
};