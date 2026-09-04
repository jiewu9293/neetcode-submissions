class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freq = new HashMap<>();
        
        for(int num:nums){
            freq.put(num,freq.getOrDefault(num,0) + 1);
        }

        List<Integer>[] buckets = new List[nums.length + 1];
        for(Map.Entry<Integer,Integer> e : freq.entrySet()){
            int f = e.getValue();
            if(buckets[f] == null) buckets[f] = new ArrayList<>();
            buckets[f].add(e.getKey());
        }

        int[] ans = new int[k];
        int idx = 0;
        for(int f = buckets.length - 1; idx < k && f > 0; f--){
            if(buckets[f] == null) continue;
            for(int n: buckets[f]){
                ans[idx++] = n;
                if(idx == k) break;
            } 
        }
        return ans;

    }
}
