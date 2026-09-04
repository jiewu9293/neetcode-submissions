//use doubly linkedlist to implement deque
//implement doubly linkedlist node
class Node{
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
    private Node dummyHead;
    private Node dummyTail;
    public Deque() {
        this.dummyHead = new Node(-1);
        this.dummyTail = new Node(-1);//set default value to head and null
        this.dummyHead.next = this.dummyTail;
        this.dummyTail.prev = this.dummyHead;

    }

    public boolean isEmpty() {
            return this.dummyHead.next == this.dummyTail;
    }

    public void append(int value) {
       //append elements from the end
    Node newNode = new Node(value);
    Node lastNode = this.dummyTail.prev;
    lastNode.next = newNode;
    newNode.prev = lastNode;
    newNode.next = this.dummyTail;
    this.dummyTail.prev = newNode;



    }

    public void appendleft(int value) {
        //append element at the start
        Node newNode = new Node(value);
        Node firstNode = this.dummyHead.next;
        
        firstNode.prev = newNode;
        newNode.next = firstNode;
        this.dummyHead.next = newNode;
        newNode.prev = this.dummyHead;
    }

    public int pop() {
        //return and remove element at the end
        if(isEmpty()){
            return -1;
        }
        Node targetNode = this.dummyTail.prev;
        Node prevNode = targetNode.prev;

        prevNode.next = this.dummyTail;
        this.dummyTail.prev = prevNode;
        return targetNode.val;

    }

    public int popleft() {
        if(isEmpty()){
            return -1;
        }
        Node targetNode = this.dummyHead.next;
            Node nextNode = targetNode.next;

            this.dummyHead.next = nextNode;
            nextNode.prev = this.dummyHead;

            return targetNode.val;
    }
}
