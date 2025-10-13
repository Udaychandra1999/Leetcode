class Solution {
public:
    int max(int a,int b) {return a>b?a:b;}
    int lengthOfLongestSubstring(string s) {
        map<char,int> mp;
        int maxLen = 0,start=0;
        for(int i=0;i<s.length();i++) {
            if (mp.find(s[i]) != mp.end() && mp[s[i]]>=start){
                start = mp[s[i]]+1;
            }
            mp[s[i]] = i;
            maxLen = max(maxLen,i-start + 1);
        }
        return maxLen;
    }
};