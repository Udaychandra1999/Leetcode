class Solution {
    public String toLowerCase(String s) {
        String res = new String();
        for(char c:s.toCharArray()){
            if (c>='A' && c<='Z'){
                res += (char)(c+32);
            }else {
                res +=c;
            }
        }
        return res;
    }
}