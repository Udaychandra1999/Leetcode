class Solution {
public:
    int abs(int x){
        if (x<0){
            return -x;
        }
        return x;
    }
    int countKeyChanges(string s) {
        int count = 0;
        for(int i=1;i<s.length();i++){
            if( s[i-1]!=s[i] && abs(s[i-1]-s[i])!=32 )
            {
                count++;
            }
        }
        return count;
    }
};