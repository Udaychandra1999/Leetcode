class Solution {
    public int[] rearrangeArray(int[] nums) {
        ArrayList<Integer> pos = new ArrayList<Integer>();
        ArrayList<Integer> neg = new ArrayList<Integer>();
        for(int i:nums)
        {
            if(i>0)
                pos.add(i);
            else
                neg.add(i);

        }
        int i,l,r;
        i=l=r=0;
        while(i<nums.length)
        {
            if(i%2==0)
            {
                nums[i] = pos.get(l);
                l++;
            }
            else
            {
                nums[i] = neg.get(r);
                r++;
            }
            i++;
        }

        return nums;
    }
}