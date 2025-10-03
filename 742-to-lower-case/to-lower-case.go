func toLowerCase(s string) string {
    result := []rune(s)
    for i,c :=range result {
        if c>='A' && c<='Z'{
            result[i] = c +32;
        }
    }
    return string(result)
}