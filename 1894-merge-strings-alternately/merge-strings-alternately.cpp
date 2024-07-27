class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res = "";
        int i=0,j=0;
        int n = word1.length();
        int m = word2.length();
        if(n==0)
            return word2;
        if(m==0)
            return word1;
        while(i<n && j<m)
        {
            res+=word1[i++];
            res+=word2[j++];
        }
        while(i<n)
        {
            res+=word1[i++];
        }
        while(j<m)
        {
            res+=word2[j++];
        }
        return res;
    }
};