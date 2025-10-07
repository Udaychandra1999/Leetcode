class Solution {
public:
    bool judgeSquareSum(int c) {
        long l,h,sn;
        l=0;
        h=sqrt(c);
        while(l<=h){
            sn = l*l+h*h;
            if(sn==c){
                return true;
            }else if(sn>c){
                h--;
            }else{
                l++;
            }
        }
        return false;
    }
};