class NumArray {
public:
    vector<int> tree;
    vector<int> nums;
    int n;
    NumArray(vector<int>& numss) {
        n = numss.size();
        tree =  vector<int>(n+1);
        nums =  numss;
        
        for(int i = 0; i <n; i ++)
        {
            for(int j = i+1; j <=n ; j += j & (-j))
            {
                tree[j] += nums[i];
            }
        }
    }
    
    void update(int index, int val) {
        int temp = val - nums[index];
        
            for(int j = index+1 ; j <= n; j += j & (-j))
            {
                tree[j] += temp;
            }
        
        tree[index] = val; 
        
    }
    
    int sumRange(int left, int right) {
        return getSum(right + 1) - getSum(left);
    }
    
    int getSum(int idx)
    {
        int s = 0;
        
        for(int j = idx ; j > 0  ; j -= j & (-j))
        {
            s += tree[j];
        }
        
        return s;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */