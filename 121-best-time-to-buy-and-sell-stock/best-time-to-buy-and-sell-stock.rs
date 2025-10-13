impl Solution {
    pub fn max(a:i32,b:i32)->i32{
        if a>b {
            a
        }else {

        b
        }
    }
    pub fn min(a:i32,b:i32)->i32{
        if a<b{
            a
        }else {
            b
        }
    }
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut res:i32 = 0;
        let mut mp:i32 = prices[0];
        for i in prices {
            mp = Solution::min(mp,i);
            res = Solution::max(res,i-mp);
        } 
        res
    }
}