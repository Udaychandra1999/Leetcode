use std::collections::HashMap;
impl Solution {
    pub fn max(a:i32,b:i32)->i32 {
        if a>b {
            return a;
        }else {
            return b;
        }
    }
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut start=0;
        let mut maxLen=0;
        let mut mp:HashMap<char,usize> = HashMap::new();
        for (i,ele) in s.chars().enumerate() {
            if let Some(idx) = mp.insert(ele,i){
                if idx>=start {
                    start = idx+1;
                }
            }
            maxLen = Self::max(maxLen,(i-start+1) as i32);
        }
        maxLen
    }
}