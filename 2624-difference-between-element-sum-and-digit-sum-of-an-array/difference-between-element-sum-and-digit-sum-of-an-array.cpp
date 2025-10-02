class Solution {
public:
    int abs(int a){
        return a>0?a:-a;
    }
    int differenceOfSum(vector<int>& nums) {
        int s,ds;
        s=0;ds=0;
        int x;
        for(int i:nums){
            s+=i;
            x = i;
            while(x>0){
                ds+=x%10;
                x /=10;
            }
        }
        return abs(s-ds);
    }
};