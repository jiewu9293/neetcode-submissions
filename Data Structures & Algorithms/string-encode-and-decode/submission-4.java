class Solution {
    
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String s: strs){
            sb.append(s.length()).append('#').append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0; // Two pointers to decode the string
        while(i < str.length()){
            int j = i;
            while(str.charAt(j)!= '#'){
                j++; // move pointer j until j is pointing to '#'
            }
            //string before # is the length, then we convert the string to int, then we get the length of the string we are going to decode
            int length = Integer.parseInt(str.substring(i,j)); // then we can go to decode the string
            i = j + 1; // i is at the start position of the string
            j = i + length; // j is at the end of the string

            res.add(str.substring(i,j)); //add the string to the res list
            i = j; // move i to the j position for the next iteration
        }
        return res; // after iteration return res list which contains all the strings after decoded
    }
    }

