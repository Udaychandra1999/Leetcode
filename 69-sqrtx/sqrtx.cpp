class Solution {
public:
    int mySqrt(int x) {
        if (x == 0 || x ==1 ){
            return x;
        }
        long  low,mid,high;
        low = 1;
        high = x;
        int res;
        while (low<=high){
            mid = (low+high)/2;
            if (mid*mid == x){
                return mid;
            }else if(mid*mid>x){
                high = mid -1;
            }else {
                res = mid;
                low = mid +1;
            }
        }
        return res;
    }
};