class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLen=0,start=0;
        HashMap<Character,Integer> mp = new HashMap<>();
        for(int i=0;i<s.length();i++){
            if(mp.containsKey(s.charAt(i)) && mp.get(s.charAt(i))>=start){
                start = mp.get(s.charAt(i))+1;
            }
            mp.put(s.charAt(i),i);
            maxLen = Math.max(maxLen,i-start+1);
        }
        return maxLen;
    }
}