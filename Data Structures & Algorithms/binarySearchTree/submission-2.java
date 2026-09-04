class TreeNode{
    int key;
    int val;
    TreeNode right;
    TreeNode left;
    public TreeNode(int key, int val){
        this.key = key;
        this.val = val;
    }
}
class TreeMap {
    private TreeNode root;
    public TreeMap() {
        this.root = null;
    }

    public void insert(int key, int val) {
        //insert the node in the treemap;
        TreeNode newNode = new TreeNode(key,val);
        if(root == null){
            root = newNode;
            return; //if bst has no elements then insert the node and set the node to be the root of bst
        }
        TreeNode curr = root; //if the bst is not empty, set the root node of the bst as the curr node
        while(true){
            if(curr.key < key){
                if(curr.right == null){
                    curr.right = newNode;
                    return; // if the key of curr is less then the key of newNode, then newNode should be inserted at the right subtree of curr
                        // if the right chile of curr is empty then insert the newnode to the right child of curr 

                }
                //if the right child of curr is not empty // keep searching in the right subtree;
                curr = curr.right;
            }
            else if(curr.key > key){
                if(curr.left == null){
                    curr.left = newNode;
                    return;
                }
                curr = curr.left;
            }
            else {
                //curr.key == key
                curr.val = val;
                return;
            }
        }
    }

    public int get(int key) {
        //return the val mapped with the input key // if not found then return -1
        TreeNode curr = root;
        while(curr != null){
            if(curr.key > key){
                curr = curr.left;
            }
            else if(curr.key < key){
                curr = curr.right;
            }
            else{
                //curr.key == key 
                return curr.val;
            }
        }
        return -1;
    }

    public int getMin() {
        //return the val of the smallest key in the tree
        TreeNode curr = findMin(root);
        //findmin return the node with the smallest key
        //ternary operator
        return (curr != null) ? curr.val : -1;
    }
    private TreeNode findMin(TreeNode node){
        while(node != null && node.left != null){
            node = node.left;
            //the smallest key is always in the left subtree
        }
        return node;
    }

    public int getMax() {
        //return the val of the max key in int bst
        TreeNode curr = findMax(root);
        return (curr != null) ? curr.val : -1;
    }
    private TreeNode findMax(TreeNode node){
        while(node != null && node.right != null){
            node = node.right;
        }
        return node;
    }

    public void remove(int key) {
       //remove a node in the bst with the input key
       this.root = removeHelper(root,key);
    }
    public TreeNode removeHelper(TreeNode curr, int key){
        if(curr == null ) return null;
        if(key > curr.key){
            curr.right = removeHelper(curr.right,key);
        }
        else if(key < curr.key){
            curr.left = removeHelper(curr.left,key);
        }
        else{
            if(curr.left == null) return curr.right;
            if(curr.right == null) return curr.left;
            else{
                // successor method, we have to replace  the cur node with the node with smallest key on the right subtree
                TreeNode minNode = findMin(curr.right); // return the node with the smallest key on the right sub tree of the curr node;
                curr.key = minNode.key;
                curr.val = minNode.val;
                curr.right = removeHelper(curr.right,minNode.key); //after replace we have delete the node in its original position;
            }
        }
        return curr;
    }

    public List<Integer> getInorderKeys() {
            List<Integer> res = new ArrayList<>();
            inorderTraversal(root,res);
            return res;
    }
    public void inorderTraversal(TreeNode node, List<Integer> res){
        if(node == null) return;
        inorderTraversal(node.left,res);
        res.add(node.key);
        inorderTraversal(node.right,res);
    }
}
