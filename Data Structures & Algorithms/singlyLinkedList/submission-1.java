class Node{
    int val;
    Node next;
    public Node(int val){
        this.val = val;
        this.next = null;
    }
}
class LinkedList {
    private Node dummyHead;
    private Node tail;

    public LinkedList() {   
        this.dummyHead = new Node(-1);
        this.tail = this.dummyHead;

    }

    public int get(int index) {
        Node curr = this.dummyHead.next;
        int i = 0;
        while(curr != null){
            if(i == index){
                return curr.val;
            }
            i++;
            curr = curr.next;
        }
        return -1;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        newNode.next = this.dummyHead.next;
        this.dummyHead.next = newNode;
        if(newNode.next == null){
            this.tail = newNode;
        }
    }

    public void insertTail(int val) {
        this.tail.next = new Node(val);
        this.tail = this.tail.next;
    }

    public boolean remove(int index) {
        int i = 0;
        Node curr = this.dummyHead;
        while(i<index && curr != null){
            i++;
            curr = curr.next;
        }

        if(curr != null && curr.next != null){
            if(curr.next == this.tail){this.tail = curr;}
            curr.next = curr.next.next;
            return true;
        }
        return false;
    }

    public ArrayList<Integer> getValues() {
            ArrayList<Integer> res = new ArrayList<>();
            Node curr = this.dummyHead.next;
            while(curr != null){
                res.add(curr.val);
                curr = curr.next;
            }
            return res;
    }
}
