class Solution {
    public int mySqrt(int x) {
        if(x==0 || x == 1){
            return x;
        }
        double rx,r;
        r =x;
        rx = (x+1)/2;
        while(rx!=r){
            r=rx;
            rx = (0.5*(r+x/r));
        }
        if(r<0){
            r = -r;
        }
        return (int)r;
    }
}