class Solution {
    public int reverse(int x) {
        long ans=0;
        boolean flag =false;
        if(x<0)
        {
            flag = true;
            x = x*-1;
        }
        while(x>0)
        {
            ans = ans*10 + x%10;
            x = x/10;
        }
        if(flag)
        {
            ans = -1*ans;
        }
        return (Integer.MIN_VALUE<ans && Integer.MAX_VALUE>ans) ? (int)ans : 0;

    }
}