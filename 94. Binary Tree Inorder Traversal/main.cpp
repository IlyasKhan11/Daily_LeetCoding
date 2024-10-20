/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    void Traverse(TreeNode* root, vector<int> &ans){
        if(root==NULL){
            return ;
        }
        Traverse(root->left,ans);
        ans.push_back(root->val);
        Traverse(root->right,ans);

    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> ans;
        Traverse(root,ans);
        return ans;
    }
};