class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> res = new ArrayList<>();
        if(nums.length==0)
        {
            return res;
        }
        int i,j;
        i=0;
        j=1;
        String s = new String();
        while(j<nums.length)
        {
            if(nums[j-1]+1 == nums[j])
            {
                j++;
            }
            else
            {
                
                if(nums[j-1]==nums[i])
                {
                    s = nums[i]+"";
                }
                else
                s = nums[i]+"->"+nums[j-1];
                i=j;
                res.add(s);
                s="";
                j++;
            }
        }
        if(i!=nums.length-1)
        {
            s = nums[i]+"->"+nums[j-1];
        }
        else
        {
            s = nums[i]+"";
        }
        res.add(s);
        return res;
    }
}