class Solution {
    public int maxArea(int[] height) {
        if (height.length ==2)
        {
            int h= Math.min(height[0],height[1]);
            return h;
        }
        int low=0,high=height.length-1;
        int h = Integer.MIN_VALUE;
        while(low<high)
        {
            int len = high-low;
            int ht;
            if(height[low]>height[high])
            {
                ht = height[high]*len;
                high--;
            }
            else
            {
                ht = height[low]*len;
                low++;
            }
            h = Math.max(h,ht);
            
        }
        return h;

    }
}