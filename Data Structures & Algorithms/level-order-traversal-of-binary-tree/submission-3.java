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
    public List<List<Integer>> levelOrder(TreeNode root) {
        //create a list of list to keep the result
        List<List<Integer>> res = new ArrayList<>();
        //create a queue to keep node at every level
        Queue<TreeNode> q = new LinkedList<>();

        //at the first root node to queue
        q.add(root);

        while(!q.isEmpty()){
            //create a list to keep the value of every node at each level
            List<Integer> level = new ArrayList<>();
            //number of iterations for the inner loop is the number of element in the queue
            for(int i = q.size(); i > 0; i--){
                //return and remove the first element in the queue
                TreeNode curr = q.poll();
                if(curr != null){
                    level.add(curr.val);
                    if(curr.left != null){
                        q.add(curr.left);
                    } //add left child to the queue
                    if(curr.right != null){
                        q.add(curr.right);
                    } //add right child to the queue
                }
            }
            if(level.size() > 0){
                res.add(level);
            }
        }
        return res;
    }
}
