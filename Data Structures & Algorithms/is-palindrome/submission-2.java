class Solution {
    public boolean isPalindrome(String s) {
        //two pointers;
        int l = 0, r = s.length() - 1;
        //left pointer at the index 0 of the string;
        //right pointer at the last index of the string;
        while(l < r){
            while(l < r && !alphaNum(s.charAt(l))){
                l++; // if l is pointing a symbol or anything that is not a number or letter, then move left pointer to the character or number
            }
            while(r > l && !alphaNum(s.charAt(r))){
                r--; 
            }
            if(Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))){
                return false; // compare the pair of char that left and right pointers are pointing to, if not equal then return false directly;
            }
            l++;r--; // if it's equal then move the pointers, and compare the next pair of char


       
    }
     return true; // if all the pair are equal then return true, the string is a palindrome
    }
    public boolean alphaNum(char c){
        //determine c is alphabet or number, or not alphabet and number
            //if c is not alphabet and not a number we return false

        return ( c >= 'A' && c <= 'Z' ||
                c >= 'a' && c <= 'z'||
                c >= '0' && c <= '9');
    }
}
