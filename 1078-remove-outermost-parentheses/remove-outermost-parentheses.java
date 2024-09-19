class Solution {
    public String removeOuterParentheses(String s) {
        int cnt=0;
        String res="";
        for(int i=0;i<s.length();i++)
        {
            if(s.charAt(i)=='(')
            {
                if(cnt!=0)
                {
                    res+=s.charAt(i);
                }
                cnt++;
            }
            else if(s.charAt(i)==')')
            {
                if(cnt!=1)
                {
                    res+=s.charAt(i);
                }
                cnt--;
            }
        }
        return new String(res);
    }
}