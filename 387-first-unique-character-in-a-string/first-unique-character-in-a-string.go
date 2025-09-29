func firstUniqChar(s string) int {
    var chars [26]int

    for _,c := range s{
        chars[c-'a']++
    }
    for i,c := range s {
        if chars[c-'a'] == 1{
            return i
        }
    }
    return -1
}