class Solution {
    public int maxProfit(int[] prices) {
        int profit,cost;
        int buy = prices[0];
        profit = 0;
        for(int i=1;i<prices.length;i++)
        {
            cost = prices[i]-buy;
            profit = Math.max(profit,cost);
            buy = Math.min(buy,prices[i]);
        }
        return profit;
    }
}