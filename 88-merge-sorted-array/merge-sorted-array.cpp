class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i,j;
        i=j=0;
        vector<int> res = nums1;
        int k=0;
        while(i<m&&j<n)
        {
            if(nums1[i]<nums2[j])
            {
                res[k++] = nums1[i++];
            }
            else
            {
                res[k++] = nums2[j++];
            }
        }
        while(i<m)
        {
            res[k++] = nums1[i++];
        }
        while(j<n)
            res[k++] = nums2[j++];
        nums1.swap(res);
    }
};