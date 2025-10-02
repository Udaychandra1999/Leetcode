impl Solution {
    pub fn abs(n:i32)-> i32{
        if n>0{
            n
        }else {
            -n
        }
    }
    pub fn difference_of_sum(nums: Vec<i32>) -> i32 {
        let mut s=0;
        let mut ds=0;
        for i in nums {
            let mut x = i;
            s += i;
            while x>0 {
                ds += x%10;
                x /= 10;
            }
        }
        Solution::abs(s-ds)
    }
}