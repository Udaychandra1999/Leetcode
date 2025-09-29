impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut ch = [0;26];

        for c in s.chars() {
            ch[(c as u8 - b'a') as usize]+=1;
        }
        for (i,c) in s.chars().enumerate(){
            if ch[(c as u8 - b'a') as usize] == 1{
                return i as i32;
            }
        }
        -1 as i32
    }
}