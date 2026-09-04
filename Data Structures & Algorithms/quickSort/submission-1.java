// Definition for a pair.
// class Pair {
//     int key;
//     String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> quickSort(List<Pair> pairs) {
        quickSortHelper(pairs, 0 , pairs.size()-1);
        return pairs; 
    }
    public void quickSortHelper(List<Pair> pairs, int s, int l){
        if(l - s + 1 <= 1) return; //basecase if number of element is 1 then just return 
         Pair pivot = pairs.get(l);
         int left = s;

         for(int i = s; i < pairs.size(); i++){
                if(pairs.get(i).key < pivot.key){
                    Pair temp = pairs.get(left);
                    pairs.set(left, pairs.get(i));
                    pairs.set(i,temp); //swap the values at index i and index left
                    left++;
                }
         }
         pairs.set(l,pairs.get(left));
         pairs.set(left,pivot); //swap the values at index left and the pivot
         
         quickSortHelper(pairs, s, left -1); // quick sort the left partition
         quickSortHelper(pairs, left+1, l); // quick sort the right partition
    }
}
