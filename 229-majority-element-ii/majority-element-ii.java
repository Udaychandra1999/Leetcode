class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        int k = nums.length/3;
        HashMap<Integer,Integer> mp = new HashMap<>();
        for(int i=0;i<nums.length;i++)
        {
            if(mp.containsKey(nums[i]))
            {
                mp.put( nums[i],mp.get(nums[i])+1 );
            }
            else
            {
                mp.put( nums[i],1 );
            }
        }
        for(Map.Entry<Integer,Integer> e : mp.entrySet())
        {
            if(e.getValue()>k)
            {
                res.add(e.getKey());
            }
        }
        return res;
    }
}