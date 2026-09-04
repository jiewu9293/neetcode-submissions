class DynamicArray {
    int[] data;
    int size;   // number of positions occupied in the array
    int capacity; //number of positions in the array
    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.data = new int[capacity];
    }

    public int get(int i) { 
        return data[i];
    }

    public void set(int i, int n) {
        data[i] = n;
    }

    public void pushback(int n) {
        if(size == capacity){
            resize();
        }
        data[size] = n;
        size++;
    }

    public int popback() {
        //remove and return the last element at the end
        return data[--size];
    }

    private void resize() {
        int[] newData = new int[capacity*=2];
        for(int i = 0; i < size; i++){
            newData[i] = data[i]; //copy element from old array to new array
        }
        data = newData;
    }

    public int getSize() {
            return size;
    }

    public int getCapacity() {
        return capacity;
    }
}
