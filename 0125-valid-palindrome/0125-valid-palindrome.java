class Solution {
    public boolean isPalindrome(String s) {
        
        String filteredStr = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        
        if (filteredStr.isEmpty()){
            return true;
        }

        int len = filteredStr.length();
        
        int ptr1 = (len / 2) - 1;
        int ptr2 = len % 2 == 0 ? len / 2 : len / 2 + 1;
        
        while(ptr1 >= 0 && ptr2 < len){
            if(filteredStr.charAt(ptr1) != filteredStr.charAt(ptr2)){
                return false;
            }
            
            ptr1 -= 1;
            ptr2 += 1;
        }
        
        return true;
    }
}