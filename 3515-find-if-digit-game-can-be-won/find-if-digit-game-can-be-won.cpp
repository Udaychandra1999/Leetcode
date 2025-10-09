class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        int total = 0;
        for(int x:nums){
            total+=x;
        }
        int alice;
        alice =0;
        //single digit case
        for(int x:nums){
            if(x<=9){
                alice+=x;
            }
        }
        if(total != alice*2){
            return true;
        }
        return false;
    }
};