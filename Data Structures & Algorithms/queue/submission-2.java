class Node{
    //used doubly linkedlist node
    int val;
    Node next;
    Node prev;
    public Node(int val){
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}
class Deque {
    private Node dummyTail;
    private Node dummyHead;
    public Deque() {
    this.dummyHead = new Node(-1);
    this.dummyTail = new Node(-1);

    this.dummyTail.prev = this.dummyHead;
    this.dummyHead.next = this.dummyTail;
    }

    public boolean isEmpty() {
            return this.dummyHead.next == this.dummyTail;
    }

    public void append(int value) {
       Node newNode = new Node(value);
       Node lastNode = this.dummyTail.prev;

       lastNode.next = newNode;
       newNode.prev = lastNode;
       newNode.next = this.dummyTail;
       this.dummyTail.prev = newNode;
    }

    public void appendleft(int value) {
        Node newNode = new Node(value);
        Node nextNode = this.dummyHead.next;

        this.dummyHead.next = newNode;
        newNode.prev = this.dummyHead;
        newNode.next = nextNode;
        nextNode.prev = newNode;
    }

    public int pop() {
        if(isEmpty()){
            return -1;
        }
        Node removed = this.dummyTail.prev;
        Node prevNode = removed.prev;

        prevNode.next = this.dummyTail;
        this.dummyTail.prev = prevNode;
        return removed.val;
    }

    public int popleft() {
        if(isEmpty()){
            return -1;
        }
        Node removed = this.dummyHead.next;
        Node nextNode = removed.next;

        nextNode.prev = this.dummyHead;
        this.dummyHead.next = nextNode;

        return removed.val;
    }
}
