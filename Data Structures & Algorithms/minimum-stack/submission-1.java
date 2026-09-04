class MinStack {
        private Stack<Integer> stack;
        private Stack<Integer> minStack; // used to store the minimum value
    public MinStack() {
       stack = new Stack<>();
       minStack = new Stack<>(); 
    }
    
    public void push(int val) {
        stack.push(val); // push element to stack as normal
        if(minStack.isEmpty() || minStack.peek() >= val){
            minStack.push(val); // top element of the minstack is always the min value of the stack
        }
    }
    
    public void pop() {
        if (stack.isEmpty()) return;
        int removed = stack.pop(); // pop element from stack as normal
                                    // but we need to use the return value to compare with the top element of the min stack
        if(removed == minStack.peek()){
            minStack.pop(); //make sure if the minimum value is not in the stack then it must not in the minstack as well
   
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
