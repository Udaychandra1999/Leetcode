class Solution {
public:
    int firstUniqChar(string s) {
        int chars[26];
        for(char c:s){
            chars[c-'a']++;
        }
        for(int i=0;i<s.size();i++){
            if(chars[s[i]-'a']==1){
                return i;
            }
        }
        return -1;
    }
};