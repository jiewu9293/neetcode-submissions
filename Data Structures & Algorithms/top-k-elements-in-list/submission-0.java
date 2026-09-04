class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freq = new HashMap<>(); // count the frequency of each number in the array
        // key of the map(freq) is the element and value of the map is the frequency of the element 
        for(int x: nums){freq.put(x,freq.getOrDefault(x,0)+1);}  // iterate the array 
        //it the number appear once then we increament its frequency
        //if the number is not in the map, then we start counting its frequency from zero

        List<Integer>[] buckets = new List[nums.length + 1];
        // create bucket , each element of the buckets is List<Integer>
        // the size of the bucket will be nums.length + 1, in case all elements in nums is the same number
        //nums = [2,2,2,2]
        // in the buckets, index means the frequency of the number in the nums;
        //eg [0] all the element appear zero time
        //  all the elements appear once  will store in [1] in the buckets
       for(Map.Entry<Integer,Integer> e: freq.entrySet()){
        int f = e.getValue();
        if(buckets[f] == null)buckets[f] = new ArrayList<>();
        buckets[f].add(e.getKey()); // if the fth bucket is not null, then we get the number from the entry and add it to the fth bucket
        // if the fth bucket is null, then we need initalise an arraylist in the bucket to hold the number
        // in the buckets, the index is frequency, values at the index will be the number with this frequency
    }

    int[] ans = new int[k]; // initialse ans array used to return as final answer
                        // its length must be k, cuz we need to return k element
    int idx = 0; // number of elements in ans
    for(int f = buckets.length -1; f >= 0 && idx < k;f--){ // we start from the highest index in the buckets which is the highest frequency
        if(buckets[f] == null) continue; // if there is no number at this frequency then we go to the next iteration
        for(int n : buckets[f]){ // iterate the number in fth bucket
           ans[idx++] = n; //add the number to the ans then increment idx
           if(idx == k) break; // if idx == k means we have collected enough numeber in the ans then we can break the for loop
        }
    }
    return ans;
    }
}
