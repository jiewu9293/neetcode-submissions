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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if(preorder.length == 0 || inorder.length == 0) return null;

        TreeNode root = new TreeNode(preorder[0]);

        int m = -1;

        for(int i = 0; i < inorder.length; i++){
            if(preorder[0] == inorder[i]){
                m = i;
                break;
            }
        }
// in inorder array m is the index for the rootnode 
// values before the root node in inorder array, are the nodes on left subtree, so m is also the number of values on the left subtree
        //start slicing array
        int[] leftPreorder = Arrays.copyOfRange(preorder,1,m+1); //slice the values on the left subtree
        int[] leftInorder = Arrays.copyOfRange(inorder,0,m);
        root.left = buildTree(leftPreorder, leftInorder); // builder the left subtree;

        int[] rightPreorder = Arrays.copyOfRange(preorder, m + 1, preorder.length);
        int[] rightInorder = Arrays.copyOfRange(inorder,m + 1, inorder.length);
        root.right = buildTree(rightPreorder, rightInorder);

        return root;
    }
}
