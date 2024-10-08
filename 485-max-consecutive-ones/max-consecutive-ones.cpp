class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count=0,max=0;
        for(int i:nums)
        {
            if (i==1)
            {
                count++;
            }
            else
            {
                if(max<count)
                {
                    max = count;
                }
                count =0;
            }
        }
        
        return count>max?count:max;
    }
};