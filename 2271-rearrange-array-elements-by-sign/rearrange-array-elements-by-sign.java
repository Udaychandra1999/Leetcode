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
        int n = nums.length/2;
        for(int i =0;i<n;i++)
        {
            nums[i*2] =  pos.get(i);
            nums[2*i+1] = neg.get(i);
        }

        return nums;
    }
}