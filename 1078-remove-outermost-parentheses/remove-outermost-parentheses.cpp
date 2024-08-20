class Solution {
public:
    string removeOuterParentheses(string s) {
        string res="";
        int cnt=0;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='(')
            {
                if(cnt!=0)
                {
                    res = res+s[i];
                }
                cnt++;
            }
            else if(s[i]==')')
            {
                if(cnt!=1)
                {
                    res = res+s[i];
                }
                cnt--;
            }
        }
        return res;
    }
};