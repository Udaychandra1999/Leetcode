class Solution {
    public int subarraySum(int[] nums, int k) {
        int s=0,count =0;
        HashMap<Integer,Integer> mp = new HashMap<>();
        mp.put(0,1);
        for(int i:nums)
        {
            s+=i;
            if(mp.containsKey(s-k))
            {
                count+=mp.get(s-k);
            }
            if(mp.containsKey(s))
            {
                mp.put(s,mp.get(s)+1);
            }
            else
            {
                mp.put(s,1);
            }
        }
        return count;
    }
}