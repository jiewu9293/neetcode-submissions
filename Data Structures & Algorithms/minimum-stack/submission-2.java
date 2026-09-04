class MinStack {
        private Stack<Integer> stack;
        private Stack<Integer> minStack;//Used to store the min value of stack
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val); // push element into the stack as normal
        if(minStack.isEmpty() || minStack.peek() >= val){
            minStack.push(val);// top element of minstack is always the min value of the stack
        }
        
    }
    
    public void pop() {
        if(stack.isEmpty()) return;
        int removed = stack.pop(); // pop the top element from the stack as normal and store the return value 
        if(removed == minStack.peek()){
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
