class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // map the value to the frequency of the value
        Map<Integer,Integer> freq = new HashMap<>();
        for(int n: nums){
            freq.put(n,freq.getOrDefault(n,0) + 1);
        }

        //create buckets
        List<Integer>[] buckets = new List[nums.length + 1];
        // index of buckets is the frequency
        // each element of buckets is list of integer
        // if a number appears once then it will be put in the bucket at index 1
        // if appears twice then it will be put in the bucket at index 2 and so on 
        for(Map.Entry<Integer,Integer> e: freq.entrySet()){
            // freq.entrySet() return a set of entry then we can iterate the returning set
            int f = e.getValue();
            if(buckets[f] == null) buckets[f] = new ArrayList<>();
            buckets[f].add(e.getKey());
        }

        int[] ans = new int[k]; //result array we will return as final answer
                            // length of the array is k cuz we need to return k elements
        int idx = 0; // index of the ans array
        for(int f = buckets.length -1; f >= 0 && idx < k ; f--){
            if(buckets[f] == null) continue;
            for(int n : buckets[f]){
                ans[idx++] = n;
                if(idx == k) break;
            }
        }
        return ans;
    }
}
