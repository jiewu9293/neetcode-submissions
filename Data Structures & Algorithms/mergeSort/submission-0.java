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
            return mergeSortHelper(pairs, 0, pairs.size()-1);
    }

public List<Pair> mergeSortHelper(List<Pair> pairs, int s , int l){
    if (l - s + 1 <= 1){
        return pairs;
    }
    int m = (s + l) / 2; // evaluate the middle index 
 
    mergeSortHelper(pairs,s,m); // sort the right half
    mergeSortHelper(pairs,m + 1, l); //sort the left half

    merge(pairs, s , m , l);

    return pairs;
}
public void merge(List<Pair> pairs, int s, int m, int l){
    List<Pair> L  = new ArrayList<>(pairs.subList(s,m+1));//copy two sorted halfed array to temp arrays
    List<Pair> R = new ArrayList<>(pairs.subList(m + 1, l + 1));

    int i = 0; //index for left array
    int j = 0; //index for right array
    int k = s; //index for arr

    while(i < L.size() && j < R.size()){
        if(L.get(i).key <= R.get(j).key){
            pairs.set(k,L.get(i));
            i++;
        }else{
            pairs.set(k,R.get(j));
            j++;
        }
        k++;
    }
    
    while(i < L.size()){
        pairs.set(k,L.get(i));
        i++;
        k++;
    }
    while(j < R.size()){
        pairs.set(k,R.get(j));
        j++;
        k++;
    }

}
}
