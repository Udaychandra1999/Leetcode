func maxProfit(prices []int) int {
    min_p := prices[0]
    res := 0
    for i:=1 ; i<len(prices);i++ {
        if min_p > prices[i] {
            min_p = prices[i];
        }
        profit :=  prices[i] - min_p
        if res < profit {
            res = profit
        } 
    }
    return res
}