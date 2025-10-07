class Solution {
    public int mySqrt(int x) {
        if(x==0||x==1){
            return x;
        }
        long low,high,mid;
        int res=0;
        low = 1;
        high = x;
        while(low<=high){
            mid = (low+high)/2;
            if(mid*mid == x){
                return (int)mid;
            }else if(mid*mid>x){
                high = mid -1;
            }else {
                res = (int)mid;
                low = mid +1;
            }
        }
        return res;
    }
}