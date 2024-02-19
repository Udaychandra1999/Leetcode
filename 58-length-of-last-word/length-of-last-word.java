import java.util.*;
class Solution {
    public int lengthOfLastWord(String s) {
        StringTokenizer st1 = new StringTokenizer(s);
        int n1 = 0;
        while(st1.hasMoreTokens())
        {
           int x = st1.nextToken().length();
           if (x!=0)
           {
               n1=x;
           }
        }
        return n1;
    }
}