class Solution {
    public int mySqrt(int x) {
        int r = x;
        int res = x;
        while(res>0){
            double rx = (0.5)*(r+x/r);
            if(rx>r){
                res = (int) (rx-r);
            }else {
                res = (int)(r-rx);
            }
            r = (int)rx;
        }
        if(r<0){
            r = -r;
        }
        return r;
    }
}