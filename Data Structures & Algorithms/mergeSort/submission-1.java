// Definition for a pair.
// class Pair {
//     public int key;
//     public String value;
//
//     public Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
class Solution {
    public List<Pair> mergeSort(List<Pair> pairs) {
            return mergeSortHelper(pairs, 0 , pairs.size()-1);
            
    }
        // s for start index, l for last index 
    public List<Pair> mergeSortHelper(List<Pair> arr, int s, int l){
            //base case
            if(l - s + 1 <= 1) return arr;

            int m = (s + l) / 2; // m for middle index

            mergeSortHelper(arr,s,m); // sort the left half
            mergeSortHelper(arr,m+1,l); // sort the right half


            merge(arr,s,m,l);

            return arr;
    }

    public void merge(List<Pair> arr, int s, int m, int l){
        //copy sorted left and sorted right into temp arrays
            List<Pair> L = new ArrayList<>(arr.subList(s,m+1));
            List<Pair> R = new ArrayList<>(arr.subList(m+1,l+1));
            int i = 0; // index for L 
            int j = 0; // index for R
            int k = s; // k is index for arr

        while(i < L.size() && j < R.size()){
            if(L.get(i).key <= R.get(j).key){
               arr.set(k,L.get(i));
                i++;
                k++;
            }else{
                arr.set(k,R.get(j));
                j++;
                k++;
            }
        }
        //if any elements remain in left half array;
        while(i < L.size()){
            arr.set(k,L.get(i));
            i++;
            k++;
        }
        while(j < R.size()){
            arr.set(k,R.get(j));
            j++;
            k++;
        }



    }
}
