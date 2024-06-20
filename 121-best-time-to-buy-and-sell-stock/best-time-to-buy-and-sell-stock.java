class Solution {
    public int max(int a,int b)
    {
        return a>b?a:b;
    }
    public int min(int a,int b)
    {
        return a<b?a:b;
    }
    public int maxProfit(int[] prices) {
        int cost,mini;
        int profit = 0;
        mini = prices[0];
        for(int i =1;i<prices.length;i++)
        {
            cost = prices[i] - mini;
            profit = max(profit,cost);
            mini = min(mini,prices[i]);
        }
        return profit;
    }
}