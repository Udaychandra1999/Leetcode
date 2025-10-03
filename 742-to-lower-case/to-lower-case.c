char* toLowerCase(char* s) {
    int len = strlen(s);
    char *res = (char *)malloc(len+1);
    for(int i=0;i<len;i++){
        if(s[i]>='A' && s[i]<='Z'){
            res[i] = s[i]+32; 
        }else {
            res[i] = s[i];
        }
    }
    res[len]='\0';
    return res;
}