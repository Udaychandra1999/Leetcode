/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* ar = (int*)malloc(wordsSize *sizeof(int));
    int idx = 0;
    for(int i=0;i<wordsSize;i++){
        int j =0;
        while(words[i][j]!='\0')
        {
            if(words[i][j]==x){
                ar[idx++]= i;
                break;
            }
            j++;
        }
    }
    *returnSize = idx;
    return ar;
}