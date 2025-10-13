class Solution {
public:
    int max(int a,int b) {return a>b?a:b;}
    int min(int a,int b) {return a<b?a:b;}
    int maxProfit(vector<int>& prices) {
        int res=0,mp=prices[0];
        for(int p:prices){
            mp = min(mp,p);
            res = max(res,p-mp);
        }
        return res;
    }
};