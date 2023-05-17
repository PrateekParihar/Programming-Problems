class Solution {
    public boolean isValid(String s) {
        Stack<Character> tracker = new Stack<>();
        
        HashMap<Character,Character> map = new HashMap<>();
        
        map.put('{','}');
        map.put('[',']');
        map.put('(',')');
        
        for (char ch : s.toCharArray()){
            if(map.containsKey(ch)){
                tracker.push(ch);
            }
            else if(tracker.isEmpty()) {
                return false;
            }
            else{
                if(ch != map.get(tracker.pop())){
                    return false;
                }
            }
        }
        
        return tracker.isEmpty();
    }
}