class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        int res = 0;
        for(int i=0;i<sentences.size();i++){
            int x =0;
            for(int j=0;j<sentences[i].size();j++){
                if (sentences[i][j] == ' ') {
                    x++;
                }
            }
            res = res>x?res:x;
        }
        return res +1;
    }
};