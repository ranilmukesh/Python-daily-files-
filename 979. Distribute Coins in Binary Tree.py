/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int ans = 0;
    public int distributeCoins(TreeNode root) {
        get_ans(root);
        
        return ans;
    }

    public int get_ans(TreeNode root){
        if(root == null) return 0;

        int left = get_ans(root.left);
        int right = get_ans(root.right);

        ans += Math.abs(left) + Math.abs(right);

        return root.val + left + right -1 ;
    }
}
