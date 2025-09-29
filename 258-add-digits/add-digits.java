class Solution {
    public int addDigits(int num) {
        if(num<10){
            return num;
        }
        int x = num;
        int s =0;
        while(x>0){
            s += x%10;
            x = x/10;
        }
        return addDigits(s);
    }
}