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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null) return  new TreeNode(val);  // base case if root == null, we use the val to create a node and return it 

        if(root.val < val){
            root.right = insertIntoBST(root.right,val); //if val is greater than root.val we go to right subtree of root to insert the value
        }
        else if(root.val > val){
            root.left = insertIntoBST(root.left,val);
        }
        return root; //after insertion we return the root of bst

    }
}