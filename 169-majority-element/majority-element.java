class Solution {
    public int majorityElement(int[] nums) {
        int ele=-1,count=0;
        for(int i:nums)
        {
            if(ele==-1)
            {
                ele = i;
                count =1;
            }
            else if(ele == i)
            {
                count++;
            }
            else
            {
                if(count>0)
                {
                    count--;
                }
                else if(count ==0)
                {
                    ele = i;
                    count =1;
                }
            }
        }
        return ele;
    }
}