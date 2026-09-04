class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
      Map<String,List<String>> res = new HashMap<>();

      for(String s : strs){
        int[] count = new int[26]; //26 letters each letter assocated with its frequency
        for(char c : s.toCharArray()){
            count[c - 'a']++;// evaluate the frequency of the occurrence of each letter in s 
        }
        StringBuilder sb = new StringBuilder();
        for(int num : count){
            sb.append(num).append("#");
        }
        String key = sb.toString();
        res.putIfAbsent(key, new ArrayList<>());
        res.get(key).add(s);
        
        
      }
      return new ArrayList<>(res.values());
    }
}
