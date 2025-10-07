class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==1){
            return true;
        }
        long long low,high;
        long long mid;
        low = 1;
        high = num;
        while(low<=high){
            mid =(low+high)/2;
            if(mid*mid == num){
                return true;
            }else if(mid*mid > num){
                high = mid -1;
            }else {
                low  = mid +1;
            }
        }
        return false;
    }
};