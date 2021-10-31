// Given an input string s, reverse the order of the words.

// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.

//Example: 
// Input: s = "the sky is blue"
// Output: "blue is sky the"
  

class Solution {
    public String reverseWords(String s) {
    
    if (s == null) return null;
    
    char[] a = s.toCharArray();
    int n = a.length;
    
    reverse(a, 0, n - 1);
    reverseWords(a, n);
    return cleanSpaces(a, n);
  }
    
    void reverse(char[] a, int i, int j) {
    while (i < j) {
      char t = a[i];
      a[i++] = a[j];
      a[j--] = t;
    }
  }
  void reverseWords(char[] a, int n) {
    int i = 0, j = 0;
      
    while (i < n) {
      while (i < j || i < n && a[i] == ' ') i++;
      while (j < i || j < n && a[j] != ' ') j++; 
      reverse(a, i, j - 1);                      
    }
  }
  
  String cleanSpaces(char[] a, int n) {
    int i = 0, j = 0;
      
    while (j < n) {
      while (j < n && a[j] == ' ') j++;             
      while (j < n && a[j] != ' ') a[i++] = a[j++]; 
      while (j < n && a[j] == ' ') j++;             
      if (j < n) a[i++] = ' ';                      
    }
  
    return new String(a).substring(0, i);
  }
 
}
