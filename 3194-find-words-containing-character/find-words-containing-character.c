/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findWordsContaining(char** words, int wordsSize, char x, int* returnSize) {
    int* ar;
    int idx = 0;
    int capacity = 4;
    ar = (int*)malloc(capacity*sizeof(int));
    if(ar == NULL){
        *returnSize = 0;
        return NULL;
    }
    for(int i=0;i<wordsSize;i++){
        int j =0;
        while(words[i][j]!='\0'){
            if(words[i][j]==x){
                if(idx==capacity){
                    capacity*=2;
                    int* temp = (int*)realloc(ar,capacity*sizeof(int));
                    if(temp == NULL){
                        *returnSize = 0;
                        return NULL;
                    }else {
                        ar = temp;
                    }
                }
                ar[idx++] = i;
                break;
            }
            j++;
        }
    }
    *returnSize = idx;
    return ar;
}