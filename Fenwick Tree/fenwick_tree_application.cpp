class Solution {
public:

    vector<int> tree;
    vector<int> nums;

    vector<int> countSmaller(vector<int>& nums) {
        int n = nums.size();

        this->nums = nums;

        int offset = (int) 1e4 + 1;

        vector<int> res(n);
        res[n - 1] = 0;

        int tree_n = offset * 2;

        tree = vector<int>(tree_n);

        // update the last val in nums
        for (int j = offset; j <= tree_n; j += j & (-j))
        {
            tree[j] += nums[n - 1];
        }

        // cout<<"ok so far"<<endl;

        for (int i = n - 2 ; i >= 0; i--)
        {
            if (nums[i] > nums[i + 1])
            {
                res[i] = res[i + 1] + 1;

                // only update if current one is larger
                for (int j = nums[i = 1] + offset; j <= n + offset; j += j & (-j))
                {
                    tree[j] += 1;
                    tree[nums[i + 1] + offset]++;
                    // cout<<'h'<<endl;
                }
            }
            else
            {
                int temp = 0;

                for (int j = nums[i] + offset; j > 0; j -= j & (-j))
                {
                    temp +=  tree[j];
                }

                res[i] = temp;
            }

            // cout<<"ok so fafarr"<<endl;


        }


        return res;


    }
};