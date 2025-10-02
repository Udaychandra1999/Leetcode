impl Solution {
    pub fn sum_of_multiples(n: i32) -> i32 {
        let mut res = 0;
        for i in 1..n+1 {
            if i%3 ==0 {
                res+=i;
            }else if i%5==0 {
                res+=i;
            }else if i%7==0 {
                res +=i;
            }
        }
        res
    }
}