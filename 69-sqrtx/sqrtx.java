class Solution {
    public int mySqrt(int x) {
        if(x==0 || x == 1){
            return x;
        }
        double rx,r;
        r = (double)x;
        rx = (0.5*(r+x/r));
        while(rx!=r){
            r=rx;
            rx = (0.5*(r+x/r));
        }
        
        return (int)r;
    }
}