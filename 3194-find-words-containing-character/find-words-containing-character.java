class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        ArrayList<Integer> res = new ArrayList<>();
        for(int i=0;i<words.length;i++){
            for(char c:words[i].toCharArray()){
                if (x == c){
                    res.add(i);
                    break;
                }
            }
        }
        return res;
    }
}