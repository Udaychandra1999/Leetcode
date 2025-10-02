impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let mut n1 =  0;
        let mut n2 = 0;
        for i in 1..n+1 {
            if i%m==0 {
                n2+=i;
            }else {
                n1+=i;
            }
        } 
        n1-n2
    }
}