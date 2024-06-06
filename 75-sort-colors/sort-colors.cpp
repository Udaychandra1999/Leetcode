class Solution {
public:
    void sortColors(vector<int>& nums) {
        int count0=0,count1=0,count2=0;
        for(int i:nums)
        {
            if(i==0)
            {
                count0++;
            }
            else if(i==1)
            {
                count1++;
            }
            else 
            {
                count2++;
            }
        }
        int i=0;
        while(i<nums.size())
        {
            while(count0>0)
                {
                    nums[i++]=0;
                    count0--;
                }
            while(count1>0)
            {
                nums[i++]=1;
                count1--;
            }
            while(count2>0)
            {
                nums[i++]=2;
                count2--;
            }
        }
    }
};