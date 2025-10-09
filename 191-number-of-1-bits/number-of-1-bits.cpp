class Solution {
public:
    int hammingWeight(int n) {
        if(n==0){
            return 0;
        }
        if((n&(n-1))==0){
            return 1;
        }
        int count = 0;
        if(n%2==1){
            count = 1;
        }
        return count+hammingWeight(n/2);
    }
};