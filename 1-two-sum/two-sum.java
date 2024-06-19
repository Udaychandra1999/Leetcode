class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> mp = new HashMap<Integer,Integer>();
        int[] re = new int[2];
        for(int i=0;i<nums.length;i++)
        {
            int n = nums[i];
            re[0] = re[1] = -1;
            int res = target -n;
            if(mp.containsKey(res))
            {
                re[0] = mp.get(res);
                re[1] = i;
                return re;
            }
            mp.put(nums[i],i);
        }
        return re;
    }
}