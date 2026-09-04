class TreeNode{
    int key;
    int val;
    TreeNode left;
    TreeNode right;
    public TreeNode(int key,int val){
        this.key = key;
        this.val = val;
    }
}
//binary search tree map
class TreeMap {
    public TreeNode root;

    public TreeMap() {
        root = null;
    }

    public void insert(int key, int val) {
        TreeNode newNode = new TreeNode(key,val);
        if(root == null){
            root = newNode;
            return;
        }
        TreeNode curr = root;
        while(true){
            if(key < curr.key){
                if(curr.left == null){
                    curr.left = newNode;
                    return;
                }
                curr = curr.left;
            }
            else if(key > curr.key){
                if(curr.right == null){
                    curr.right = newNode;
                    return;
                }
                curr = curr.right;
            }
            else{
                curr.val = val;
                return;
            }
        }

    }

    public int get(int key) {
        TreeNode curr = root;
        while(curr != null){
            if(key < curr.key){
                curr = curr.left;
            }
            else if(key > curr.key){
                curr = curr.right;
            }else{
                return curr.val;
            }
        }
        return -1; //if the key is not the tree return -1 
    }

    public int getMin() {
        //return the val mapped to the smallest key
        TreeNode curr = findMin(root);
        return (curr != null) ? curr.val : -1;

    }
    private TreeNode findMin(TreeNode node){
        while(node != null && node.left != null){
            node = node.left;
        }
        return node;
        //in bst the smallest node is always on the left side
    }

    public int getMax() {
        //return the value mapped to the biggest key
        TreeNode curr = findMax(root);
        return (curr != null) ? curr.val : -1;
    }
    private TreeNode findMax(TreeNode node){
        //return the node with the max key value in bst
        while(node != null && node.right != null){
            node = node.right;
        }
        return node;
    }

    public void remove(int key) {
       this.root = removeHelper(root,key); //assign the root of the bst that after remove the node with the input key, to root field 
    }
    private TreeNode removeHelper(TreeNode curr, int key){
        if(curr == null) return null;
        if(key > curr.key){
           curr.right = removeHelper(curr.right,key);
        }
        else if(key < curr.key){
            curr.left = removeHelper(curr.left,key);
        }
        else{
            if(curr.left == null) return curr.right;
            else if(curr.right == null) return curr.left;
            else{
                TreeNode minNode = findMin(curr.right);
                curr.key = minNode.key;
                curr.val = minNode.val;
                curr.right = removeHelper(curr.right,minNode.key);
            }
            
        }
        return curr;

    }

    public List<Integer> getInorderKeys() {
        List<Integer> res = new ArrayList<>();
        inorderTraversal(root,res);
        return res;
    }
    public void inorderTraversal(TreeNode root, List<Integer> keys){
        if(root == null) return;
        inorderTraversal(root.left,keys);
        keys.add(root.key);
        inorderTraversal(root.right,keys);
    }
}
