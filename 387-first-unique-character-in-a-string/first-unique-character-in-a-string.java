class Solution {
    public int firstUniqChar(String s) {
       int chars[] = new int[26];
       int strlen = s.length(); 
       for(int i=0;i<strlen;i++){
        chars[s.charAt(i)-'a']++;
       }
       for(int i=0;i<strlen;i++){
        if(chars[s.charAt(i)-'a']==1){
            return i;
        }
       }
       return -1;
    }
}